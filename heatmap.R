
library(argparser)
library(pheatmap)
argv <- arg_parser('')
argv <- add_argument(argv, "--diff_dir", help="the diff dir")
argv <- add_argument(argv, "--geneID", help="gene ID")
argv <- add_argument(argv, "--compare", help="compare.txt")
argv <- add_argument(argv, "--fpkm_group", help="fpkm.xls")
argv <- add_argument(argv, "--out_dir", help="the output directory")
argv <- parse_args(argv)

diff_dir <- argv$diff_dir
geneID <- argv$geneID
compare <- argv$compare
fpkm_group <-argv$fpkm_group
out_dir <- argv$out_dir

############################File preparation######################################################################


fpkm_file <- read.delim(fpkm_group, header=TRUE)
if (is.na(geneID)){
  compare_file <- read.delim(compare, header=FALSE)
  compare_sig_matrix <- NULL
  for (i in 1:nrow(compare_file)){
    compare_name <- paste(compare_file[i,1],'vs',compare_file[i,2],sep="")
    diff_file <- read.delim(paste(diff_dir, "/", compare_name, '/',compare_name,'.Differential_analysis_results.txt',sep=''), header=TRUE, row.names=1)
    geneID_sig <-data.frame(rownames(subset(diff_file, diff_file$significant=="TRUE")))
    compare_sig_matrix <- rbind(compare_sig_matrix, geneID_sig)
  }
  unionion_ID <- data.frame(compare_sig_matrix[!duplicated(compare_sig_matrix[, 1]),])
  unionion_fpkm <- subset(fpkm_file, geneID %in% unionion_ID[, 1])
  colnames(unionion_fpkm) <- c(colnames(fpkm_file))
  write.table(unionion_fpkm, file=paste(out_dir, '/union_for_cluster', sep=""), quote=FALSE, col.names = TRUE, row.names = FALSE,sep = "\t")
  
}else{
  geneID_file <- read.delim(geneID, header=TRUE)
  rownames(fpkm_file) <- fpkm_file[,1]
  print(geneID_file[,1])
  unionion_fpkm <- subset(fpkm_file, rownames(fpkm_file) %in% geneID_file[,1])
}

#####################comparison###################################################################################

rownames(unionion_fpkm) <- unionion_fpkm[,1]
unionion_fpkm <- unionion_fpkm[, -1]
#unionion_fpkm <- log10(unionion_fpkm + 1)
if(length(unionion_fpkm[,1])<= 100){
  showname <- TRUE
}else{
  showname <- FALSE
}

if(length(unionion_fpkm[1,])<=10){
  cell_widths <- 36
  cell_width <- 34
}else{
  cell_widths <- floor(600/length(unionion_fpkm[1,]))
  cell_width <- floor(300/length(unionion_fpkm[1,]))
}

num <- length(unionion_fpkm[,1])
if(dim(unionion_fpkm)[2]==2){
  scale_row_col = "column"
}else{
  scale_row_col = "row"
}
png(paste(out_dir, "/heatCluster.png", sep=""), type="cairo-png", res=1200, width = 12, height = 6, units = 'in')
pheatmap(unionion_fpkm, 
         color=colorRampPalette(rev(c("red", "white", "blue")))(100),
         cluster_cols = T,
         scale = scale_row_col,
         legend = T,
         show_rownames = showname,
         cellwidth = cell_widths,
         fontsize = cell_widths,
         main = "Cluster analysis of differentially expressed genes")
dev.off()
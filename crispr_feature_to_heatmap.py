import argparse
import csv
"""
This script is used to convert CRISPR features csv file to heatmap format
"""
parser = argparse.ArgumentParser()
parser.add_argument('--input',help='original file')
parser.add_argument('--output_prefix',help='new format')
argv = vars(parser.parse_args())

#==============================判断参数==============================

if argv['input'] == None:
	raise Exception ('You should provide a input file!')
else:
	input=argv['input'].strip()

if argv['output_prefix'] == None:
	raise Exception ('You should provide a output file!')
else:
    output_prefix=argv['output_prefix'].strip()
input = open(input)
heatmap = open(output_prefix+"_heatmap.tsv", 'w')
header = input.readline()
header_featurename = header.strip().split(",")[1]
header_sg_RNA_info = header.strip().split(",")[2:]
print(header_sg_RNA_info[2::6])
header_sg_RNA =[ x.strip().split(",")[0].split(".")[-2] for x in header_sg_RNA_info[2::6]]
heatmap.write(header_featurename+"\t"+"\t".join(header_sg_RNA)+"\n")

for eachline in input:
    eachline = eachline.strip().split(',')
    FeatureID = eachline[0]
    FeatureName = eachline[1]
    sg_RNA_info = eachline[2:]
    sg_RNA = sg_RNA_info[1::3]
    heatmap.write(FeatureName +"\t"+"\t".join(sg_RNA)+"\n")





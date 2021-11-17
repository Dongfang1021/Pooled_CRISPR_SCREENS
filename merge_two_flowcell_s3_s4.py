import argparse

"""
This script is used to generate clonotype sequence and counts info
"""
parser = argparse.ArgumentParser()
parser.add_argument('--input_1',help='original file')
parser.add_argument('--input_2',help='original file')
parser.add_argument('--output_prefix',help='output_prefix')


argv = vars(parser.parse_args())

if argv['input_1'] == None:
	raise Exception ('You should provide a input file!')
else:
	input_1=argv['input_1'].strip()

if argv['input_2'] == None:
	raise Exception ('You should provide a input file!')
else:
	input_2=argv['input_2'].strip()


if argv['output_prefix'] == None:
    	raise Exception ('You should provide output prefix!')
else:
	output_prefix=argv['output_prefix'].strip()

input_a = open(input_1)
header_a = input_a.readline().strip().split("\t")
row_name = header_a[0]
name_a = []
for eachone in header_a[1:]:
    eachone = eachone.strip().split(' ')
    #new_name = "S1_"+ eachone[0].strip()
    new_name = "S3_"+ eachone[0].strip()
    #new_name = eachone.strip()
    name_a.append(new_name)
name_a.insert(0, row_name)
header_a = name_a

print(header_a)
dict_a = {}
for eachline in input_a:
    eachline = eachline.strip().split("\t")
    gene_name = eachline[0]
    sg_RNA = eachline[1:]
    dict_a[gene_name] = sg_RNA

input_b = open(input_2)
header_b = input_b.readline().strip().split("\t")
name_b = []
for eachone in header_b[1:]:
    eachone = eachone.strip().split(' ')
    #new_name = "S2_"+ eachone[0].strip()
    new_name = "S4_"+ eachone[0].strip()
    #new_name = eachone.strip()
    name_b.append(new_name)

print(name_b)
dict_b = {}
for eachline in input_b:
    eachline = eachline.strip().split("\t")
    gene_name = eachline[0]
    sg_RNA = eachline[1:]
    dict_b[gene_name] = sg_RNA



output = open(output_prefix+".tsv", 'w')
output.write("\t".join(header_a)+"\t"+"\t".join(name_b)+"\n")
for each_key in dict_a:
    line_a = "\t".join(dict_a[each_key])
    line_b = "\t".join(dict_b[each_key])
    output.write(each_key + "\t"+line_a + "\t" + line_b +"\n")
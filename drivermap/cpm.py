import argparse
import csv

parser = argparse.ArgumentParser()
parser.add_argument('--input',help='original file')
parser.add_argument('--output',help='new format')
argv = vars(parser.parse_args())

#==============================判断参数==============================

if argv['input'] == None:
	raise Exception ('You should provide a input file!')
else:
	input=argv['input'].strip()

if argv['output'] == None:
	raise Exception ('You should provide a output file!')
else:
    output=argv['output'].strip()
input = open(input)
output = open(output, 'w')
mulitiplied_list = []
rows = []
for eachline in input:
    eachline = eachline.strip().split("\t")
    gene = eachline[0]
    count = eachline[1:]
    if count[0].startswith("1|") or count[0].startswith("2|") or count[0].startswith("4|"):
        row = '\t'.join(count)
    else:
        mulitiplied_list = [str(float(i)*1000000) for i in count]
        row = '\t'.join(mulitiplied_list)
    output.write(gene+'\t'+ row+"\n")

    
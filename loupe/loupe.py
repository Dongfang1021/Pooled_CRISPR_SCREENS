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
rows = []
for eachline in input:
    eachline = eachline.strip().split(',')
    barcode = eachline[0]
    name = eachline[1]
    if name[0].isdigit():
        target_gene = name.strip().split('.')[-1]
    elif name == "Protospacer Per Tag":
        target_gene = "Protospacer Per Tag"
    else:
        target_gene = "Unagssigned"
    list = [barcode, target_gene]
    rows.append(list)

with open(output, 'w') as f:    
    writer = csv.writer(f)
    writer.writerows(rows)
    
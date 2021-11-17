import argparse
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt



parser = argparse.ArgumentParser()
parser.add_argument('--input',help='original file')
parser.add_argument('--output',help='new format')
argv = vars(parser.parse_args())

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
for eachline in input:
    path = eachline.strip()
    flowcell= eachline.strip().split("/")[1]
    sample = eachline.strip().split("/")[2]
    cmd_IL32='''
    grep "Feature Name" %s > boxplot/%s_%s_IL32
    grep "IL32" %s >> boxplot/%s_%s_IL32
    python Code/Violin.py --input boxplot/%s_%s_IL32 --output boxplot/%s_%s_IL32.png
    '''%(path, flowcell, sample, path, flowcell, sample, flowcell, sample, flowcell, sample)
    cmd_RELB='''
    grep "Feature Name" %s > boxplot/%s_%s_RELB
    grep "RELB" %s >> boxplot/%s_%s_RELB
    python Code/Violin.py --input boxplot/%s_%s_RELB --output boxplot/%s_%s_RELB.png
    '''%(path, flowcell, sample, path, flowcell, sample, flowcell, sample, flowcell, sample)

    cmd_TNF711='''
    grep "Feature Name" %s > boxplot/%s_%s_ZNF711
    grep "ZNF711" %s >> boxplot/%s_%s_ZNF711
    python Code/Violin.py --input boxplot/%s_%s_ZNF711 --output boxplot/%s_%s_ZNF711.png
    '''%(path, flowcell, sample, path, flowcell, sample, flowcell, sample, flowcell, sample)
    output.write(cmd_IL32 +"\n")
    output.write(cmd_RELB+"\n")
    output.write(cmd_TNF711+"\n")

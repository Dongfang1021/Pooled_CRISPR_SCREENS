#!/usr/bin/env python
#coding=utf-8
'''
Created on Oct 5, 2021
author: Dongfang Hu
Email:df2019@gmail.com
'''
import os
import sys
import glob
import argparse
import argparse
parser=argparse.ArgumentParser(prog='10Xoutdirsummary',usage='%(prog)s [opthions] [value]',description='This program is used to produce outdir summary!')
parser.add_argument('-IN','--input',help='the input file',metavar='')
parser.add_argument('-OU','--outdir',help='the output dir',metavar='')
argv=vars(parser.parse_args())

#argparse
if argv['input'] == None:
    raise Exception('You should provide input file')
else:
    input=argv['input'].strip()
if argv['outdir'] == None:
    outdir=os.getcwd()
else:
    outdir=argv['outdir'].strip()
    sample = outdir.split('/')[-1]
input = open(input,"r")
output = open(outdir+"/CRISPR.summary.txt","w")

#Sequencing,Mapping,Cells
header = input.readline().strip().split(",")
info = input.readline().strip().replace('",',':').replace('%,','%:').replace('"','').split(":")
output.write("[Sequencing]"+"\t"+sample+"\n"+header[19][8:]+"\t"+info[19]+"\n"+header[20][8:]+"\t"+info[20]+"\n"+header[21][8:]+"\t"+info[21]+"\n"+header[22][8:]+"\t"+info[22]+"\n"+header[23][8:]+"\t"+info[23]+"\n"+header[24][8:]+"\t"+info[24]+"\n"
+header[25][8:]+"\t"+info[25]+"\n"
"[Mapping]"+"\t"+sample+"\n"+header[26][8:]+"\t"+info[26]+"\n"+header[27][8:]+"\t"+info[27]+"\n"+header[28][8:]+"\t"+info[28]+"\n"+header[29][8:]+"\t"+info[29]+"\n"+header[30][8:]+"\t"+info[30]+"\n"
"[Cells]"+"\t"+sample+"\n"+header[31][8:]+"\t"+info[31]+"\n"+header[32][8:]+"\t"+info[32]+"\n"+header[33][8:]+"\t"+info[33]+"\n"+header[34][8:]+"\t"+info[34])
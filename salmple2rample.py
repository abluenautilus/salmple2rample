#!/usr/bin/env python

import os
import argparse
import shutil

parser = argparse.ArgumentParser()
parser.add_argument("input", help="squid salmple format input folder")
parser.add_argument("output", help="folder for rample formout output")
parser.add_argument("numchannels", help="number of output channels (1-8)")
args = parser.parse_args()
inputfolder = args.input
outputfolder = args.output
numchannels = int(args.numchannels)

if not os.path.exists(inputfolder):
    print("Input folder not found.")
    exit()

if not os.path.exists(outputfolder):
    os.mkdir(outputfolder)

banks = os.listdir(inputfolder)
banks = [elem for elem in banks if os.path.isdir("%s/%s" % (inputfolder,elem))]
banks.sort()
numbanks = len(banks)
print("Input banks detected: %d" % numbanks)

for i,bank in enumerate(banks):
    fullbankpath = "%s/%s" % (inputfolder,bank)
    samplefolders = os.listdir(fullbankpath)
    samplefolders.sort()
    numsamplefolders = len(samplefolders)
    outbankpath = "%s/%s" % (outputfolder,bank)
    if not os.path.exists(outbankpath):
        os.mkdir(outbankpath)

    for x in range(1,numchannels + 1):
        fullfolderpath = "%s/%d" % (fullbankpath,x)
        samples = os.listdir(fullfolderpath)
        samplepath = "%s/%s" % (fullfolderpath,samples[0])
        outputpath = "%s/%s/%d_%s" % (outputfolder,bank,x,samples[0])
        print("Will copy %s to %s" % (samplepath, outputpath))
        shutil.copy(samplepath,outputpath)
        
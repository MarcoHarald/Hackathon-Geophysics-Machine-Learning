# -*- coding: utf-8 -*-
"""
Pass all TIFF documents in the current directory, and subdirectory through Tesseract

"""

import glob
import os, argparse

def find_tiffs(inDir):
    out=[]
    for filename in glob.iglob(inDir + '/*.tif', recursive=True):
        out.append(filename)
    return out

parser = argparse.ArgumentParser()
parser.add_argument("-d", "--dir",
                    help="the directory to process")
args = parser.parse_args()

tiffs = []

if (args.dir):
    print("Will look for TIFFS in directory", args.dir)
    tiffs = find_tiffs(args.dir)
else:
    print("Will look for TIFFs in the current directory")
    tiffs = find_tiffs(".")

print("Found", len(tiffs), "TIFFs to process")
print(tiffs[1])

for tiff in tiffs:
    print(f"Converting {tiff}")
    # .txt is appended automatically...
    os.system(f"tesseract {tiff} {tiff}")
# -*- coding: utf-8 -*-
"""
Pass all PDF documents in the current directory, and subdirectory through Tika, and ideally through Tesseract if required

"""

import glob
import os, argparse

def find_docs(dir, ext="pdf"):
    out=[]
    for filename in glob.iglob(dir + f'/*.{ext}', recursive=True):
        out.append(filename)
    return out

parser = argparse.ArgumentParser()
parser.add_argument("-d", "--dict",
                    default="words.txt",
                    help="the dictionary to process")
args = parser.parse_args()

pdfs = []

print("Will read valid english words from", args.dict)

dict = {}
with open(args.dict, 'r') as f:
    word = f.readline()
    dict[word] = 1

print("Read dictionary.")

files = find_docs(".", "txt")
print("Will process", len(files), "files")
for file in files:
    

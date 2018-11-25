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
parser.add_argument("-d", "--dir",
                    help="the directory to process")
args = parser.parse_args()

pdfs = []

if (args.dir):
    print("Will look for PDFs in directory", args.dir)
    docs = find_docs(args.dir, "pdf")
else:
    print("Will look for PDFs in the current directory")
    docs = find_docs(".", "pdf")

print("Found", len(docs), "PDFs to process")
print(docs[1])

for doc in docs:
    print(f"Converting {doc}")
    # .txt is appended automatically...
    if "20_" in doc and not os.path.isfile(f'{doc}.txt'):
        os.system(f'curl -T {doc} http://localhost:9998/tika --header "Content-type: application/pdf" --header "X-Tika-PDFextractInlineImages: false" > {doc}.txthttp://localhost:9998/tika --header "Content-type: application/pdf" --header "X-Tika-PDFextractInlineImages: true" > {doc}.txt')
    else:
        print(f'Skipping {doc}')
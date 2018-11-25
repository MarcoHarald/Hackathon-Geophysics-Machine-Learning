# -*- coding: utf-8 -*-
"""
Pass all Machine Readable PDF documents in the current directory through Tika

"""

import PyPDF2
import glob
import os, argparse

def find_docs(dir, ext="pdf"):
    out=[]
    for filename in glob.iglob(dir + f'/*.{ext}', recursive=True):
        out.append(filename)
    return out

def machine_readable(doc):
    try:
        pdf = PyPDF2.PdfFileReader(doc)
        #discerning the number of pages will allow us to parse through all #the pages
        num_pages = pdf.numPages
        count = 0
        text = ""
        print("Checking", doc, "with", num_pages, "pages")
        #The while loop will read each page
        while count < num_pages:
            text += pdf.getPage(count).extractText()
            count +=1
            if len(text) > 50:
                return True
        return False
    except:
        print("Error in determining machine readability of", doc)
        return False

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
    if not os.path.isfile(f'{doc}.txt') and machine_readable(doc):
        os.system(f'curl -T {doc} http://localhost:9998/tika --header "Content-type: application/pdf" --header "X-Tika-PDFextractInlineImages: false" > {doc}.txthttp://localhost:9998/tika --header "Content-type: application/pdf" --header "X-Tika-PDFextractInlineImages: true" > {doc}.txt')
    else:
        print(f'Skipping {doc}')
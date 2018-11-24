import PyPDF2
import glob
import os

def reader(input_file):
    active_file = open(input_file)
    read_pdf = PyPDF2.PdfFileReader(input_file)
    num_pages = read_pdf.getNumPages()
    page = read_pdf.getPage(0)
    page_cont = page.extractText()
    print (page_cont)

def find_pdfs(inDir):
    out = []
    for filename in glob.iglob(inDir + '**/*.pdf', recursive=True):
        out.append(filename)

    return out

def get_cwd():
    cwd = os.getcwd()
    return out






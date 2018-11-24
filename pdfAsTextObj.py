import PyPDF2
import find_pdfs
import re


class pdfAsText:
#Pdf as text object - stores bame of pdf file, page count, pdf as text,
#and blank page count
    def __init__(self, filename):
        
        
        self.text = self.pdfFile2Text(filename)
        self.numPages = len(self.text)
        self.numBlankPages = self.countBlanks(self.text)
        self.filename = filename
        
    def checkIfBlank(self, inStr):
            #Checks if string is blank
            noWS =  re.sub(r'[\s]+','',inStr)
            if  noWS=='':
                return True
            else:
                return False
    
    def countBlanks(self, textArr):
        out = 0
        for s in textArr:
            if self.checkIfBlank(s):
                out+=1
        return out 
        
    def pdfFile2Text(self, filename):
        #Takes a pdf filepath and returns a text file, count of blank pages, 
        #and count of pages
        pdfFileObj = open(filename,'rb') 
        
        pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
        

        num_pages= pdfReader.numPages

        out = []

        for i in range(num_pages):
            pageObj = pdfReader.getPage(i) 
            page_text = pageObj.extractText()
            out.append(page_text)


        return out

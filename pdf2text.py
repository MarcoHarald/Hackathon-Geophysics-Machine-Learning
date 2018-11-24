
import pdfAsTextObj

files_dir = '../../inputs/pdfs/'




def getTextFiles(inDir, fileRange =None):
#Gets all pdf files as text and  puts in dictionarym, key is file location,
# and count of 
    ls =find_pdfs.find_pdfs(inDir)
    out = {}
    if fileRange:
        for l in ls[fileRange[0]:fileRange[1]]:
            p  =pdfAsTextObj.pdfAsText(l)
            out[l] = ( p)
    else:
        for l in ls:
            p  =pdfAsTextObj.pdfAsText(l)
            out[l] = ( p)
            
    return out


ll = getTextFiles(files_dir)
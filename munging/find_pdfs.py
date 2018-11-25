import glob


def find_pdfs(inDir):
#Returns list of pdf files within inDir
    out=[]
    for filename in glob.iglob(inDir + '**/*.pdf', recursive=True):
        out.append(filename)
        
    return out



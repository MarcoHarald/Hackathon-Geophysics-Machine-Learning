import glob


def find_pdfs(inDir):
    out=[]
    for filename in glob.iglob(inDir + '**/*.pdf', recursive=True):
        out.append(filename)
        
    return out



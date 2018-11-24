from fileFunctions import reader, find_pdfs, get_cwd

#define current working directory
file_path = get_cwd()
print (file_path)

#define source file path
path_source = '/Users/Harald/Desktop/181124 Hackathon Machine Learning Subsurface/Data/Geochem reports canada'

path_files = find_pdfs(path_source)

print (len(path_files))

#file reader
for i in path_files:
    reader(i)

print ('Done')

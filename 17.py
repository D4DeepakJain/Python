fName = input('Enter file name')
reader = open(fName,'r')
docValue  = reader.read()
reader.close()
docSplit = docValue.split(' ')
print(docSplit)
dict = {}
for i in docSplit:
    if i in dict.keys() :
        print('')
    else:
        dict[i.lower()] = 1    
print(sorted(dict.keys()))
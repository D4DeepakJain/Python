inFile= input('enter first file')
outFile= input('enter Second file')

fRead = open(inFile,'r')

fWrite=open(outFile,'w')
fWrite.write(fRead.read())
fRead.close()
fWrite.close()
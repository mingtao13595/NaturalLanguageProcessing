# coding: UTF-8
#!/usr/bin/env python
f        = open('./file/hightemp.txt', 'r')
fileList = []

for line in f:
	lineList = line[:-1].split('\t')
	fileList.append(lineList[0])
f.close()

duplicateDeleteList = set(fileList)

print(duplicateDeleteList)

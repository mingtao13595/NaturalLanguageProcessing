# coding: UTF-8
#!/usr/bin/env python
f = open('./file/hightemp.txt', 'r')
fileList = []

record_num = 0
for line in f:
	lineList = line[:-1].split('\t')
	fileList.append({
		"id"  :record_num,
		"pref":lineList[0],
		"area":lineList[1],
		"temp":lineList[2],
		"dete":lineList[3]
	})
	record_num+=1
f.close()

estmateList = {}
for i in range(len(fileList)):
	estmateList[i] = fileList[i]["temp"]
sort_estmateList = sorted(estmateList.items(), key=lambda x:x[1])

print(sort_estmateList)
estmateFileList = []
for record in fileList:
	if record["id"] = sort_estmateList[]


for line in sort_estmateList
	for i in range(len(fileList))
		estmateFileList.append(fileList[i]["id"]);

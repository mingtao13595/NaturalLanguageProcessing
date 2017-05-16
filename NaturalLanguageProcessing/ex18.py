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

lineList.sort(key=lambda x:x[0])
lineList.sort(key=lambda x:x[2])
print (lineList)

# temp = []
# for record in fileList:
#
#
# 	temp.append(record["temp"])
#
# sorted(temp)

# sort_inverse_tmp_list = []
# for line in fileList["temp"]:
# 	sort_inverse_tmp_list.append(line)
#
# print(sort_inverse_tmp_list)
# print(fileList["temp"][1]["temp"])
# print(fileList)

# sort_inverse_tmp_list = sorted(fileList["temp"]["temp"])

# print(fileList["temp"])
#
# sort_inverse_tmp_list = {
# 	"pref":[],
# 	"area":[],
# 	"temp":[],
# 	"dete":[]
# }
#
# for i in range(fileListLength):
# 	sort_inverse_tmp_list["pref"].append(lineList[0])
# 	sort_inverse_tmp_list["area"].append(lineList[1])
# 	sort_inverse_tmp_list["temp"].append(lineList[2])
# 	sort_inverse_tmp_list["dete"].append(lineList[3])

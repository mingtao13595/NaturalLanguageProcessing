# coding: UTF-8
#!/usr/bin/env python
f = open('./file/hightemp.txt', 'r')
fileList = {}

# 処理をする連想配列の定義
record_num = 0
for line in f:
	lineList = line[:-1].split('\t')
	fileList[record_num] = {
		"id"  :record_num,
		"pref":lineList[0],
		"area":lineList[1],
		"temp":lineList[2],
		"dete":lineList[3]
	}
	record_num+=1
f.close()

# ソート
sort_fileList = sorted(fileList.items(), key=lambda x:x[1]["temp"])

# 表示の処理
resultList = []
for element in sort_fileList:
	# 値だけのリスト型に変換している
	element_val = list(element[1].values())
	# 番号削除
	del element_val[0]
	resultList.append(element_val)

print(resultList)

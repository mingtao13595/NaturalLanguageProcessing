# coding: UTF-8
#!/usr/bin/env python
f = open('./file/hightemp.txt', 'r')

# ファイルデータの配列
fileList = {}
# 県だけ抜き出した配列
prefList = []
record_num = 0
for line in f:
	lineList = line[:-1].split('\t')
	fileList[record_num] = {
		"id"       :record_num,
		"pref"     :lineList[0],
		"area"     :lineList[1],
		"temp"     :lineList[2],
		"dete"     :lineList[3],
		"frequency":0
	}
	record_num+=1
	prefList.append(lineList[0])
f.close()

# 県の種類
duplicateDeletePrefList = set(prefList)
# 頻度を図る配列を定義
prefFrequencyList = {}
for pref in duplicateDeletePrefList:
	prefFrequencyList[pref] = 1

# 頻度計算
for pref_uniue in duplicateDeletePrefList:
	for pref in prefList:
		if pref_uniue == pref:
			prefFrequencyList[pref] += 1

# 頻度計算の配列をソート
sort_prefFrequencyList = sorted(prefFrequencyList.items(), key=lambda x:x[1], reverse=True)

sort_fileList = []
for record in fileList.values():
	for pref in sort_prefFrequencyList:
		# if pref[0] == record["pref"]:
		if record["pref"] == pref[0]:
			record["frequency"] = pref[1]

# ソート
sort_prefFrequencyList = sorted(fileList.items(), key=lambda x:x[1]["frequency"], reverse=True)

print(sort_prefFrequencyList)

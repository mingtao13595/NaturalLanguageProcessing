# coding: UTF-8
#!/usr/bin/env python

import re
# import json

# def morphologicalAnalysis(text, writeFile):
def morphologicalAnalysis(text):
	text_line = re.sub(r"\.|\;|\:|\?|\!", ' ', text)
	# 結果を行単位で分割
	rowList = text_line.split(' ')
	return rowList
	# wordAnalysisList = []
	# for line in rowList:
	# 	wordAnalysis = re.sub(r'\\t', ',', line)
	# 	wordAnalysis = re.sub(r'\'', '', wordAnalysis)
	# 	wordAnalysis = re.sub(r',', '_', wordAnalysis)
	# 	wordAnalysisList.append(wordAnalysis)
	# 結果を配列へ格納
	# wordAnalysisSplitList = []
	# for line in wordAnalysisList:
	# 	wordAnalysisSplitList.append(line.split("_"))

			# ファイルへの書き込み
			# json.dump(morpheme_place, writeFile, ensure_ascii=False, indent='\t', sort_keys=True, separators=(',', ': '))
			# writeFile.write(",\n")

f = open('./file/nlp.txt', 'r')
# 追記モードでファイルを開く
# rf = open('./file/ex50.json', 'a')
# rf.write("[\n")
# count = 0
result_line = []
for line in f:
	# morphologicalAnalysis(line, rf)
	result_line.extend(morphologicalAnalysis(line))
# json.dump({"end":"終"}, rf, ensure_ascii=False, indent='\t', sort_keys=True, separators=(',', ': '))
# rf.write("\n]")

# print(result_line)

for line in result_line:
	print(line)

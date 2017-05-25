# coding: UTF-8
#!/usr/bin/env python

import MeCab
import re
import json

# def morphologicalAnalysis(text):
def morphologicalAnalysis(text, writeFile):
	m = MeCab.Tagger ("mecabrc")
	mp = m.parse (text)
	# 不可視文字を表示
	mp_esc_seq = repr(mp)
	# 結果を行単位で分割
	rowList = mp_esc_seq.split(r"\n")
	wordAnalysisList = []
	for line in rowList:
		wordAnalysis = re.sub(r'\\t', ',', line)
		wordAnalysis = re.sub(r'\'', '', wordAnalysis)
		wordAnalysis = re.sub(r',', '_', wordAnalysis)
		wordAnalysisList.append(wordAnalysis)
	# 結果を配列へ格納
	wordAnalysisSplitList = []
	for line in wordAnalysisList:
		wordAnalysisSplitList.append(line.split("_"))

	# print("\n")
	# for line in wordAnalysisSplitList:
	# 	print(line)

	morpheme_list  = []
	morpheme_place = {}

	for tmp_list in wordAnalysisSplitList:
		for i in range(len(tmp_list)):
			if i % 10 == 0:
				morpheme_place["surface"] = tmp_list[i]
			elif i % 10 == 1:
				morpheme_place["base"]    = tmp_list[i]
			elif i % 10 == 2:
				morpheme_place["pos"]     = tmp_list[i]
			elif i % 10 == 3:
				morpheme_place["pos1"]    = tmp_list[i]
			elif i % 10 == 4:
				morpheme_place["pos2"]    = tmp_list[i]
			elif i % 10 == 5:
				morpheme_place["pos3"]    = tmp_list[i]
			elif i % 10 == 6:
				morpheme_place["pos4"]    = tmp_list[i]
			elif i % 10 == 7:
				morpheme_place["pos5"]    = tmp_list[i]
			elif i % 10 == 8:
				morpheme_place["pos6"]    = tmp_list[i]
			elif i % 10 == 9:
				morpheme_place["pos7"]    = tmp_list[i]
				# ファイルへの書き込み
				json.dump(morpheme_place, writeFile, ensure_ascii=False, indent='\t', sort_keys=True, separators=(',', ': '))
				writeFile.write(",\n")

f = open('./file/neko.txt', 'r')
# 追記モードでファイルを開く
rf = open('./file/ex30_practice.json', 'a')
rf.write("[\n")
count = 0
for line in f:
	morphologicalAnalysis(line, rf)
json.dump({"end":"終"}, rf, ensure_ascii=False, indent='\t', sort_keys=True, separators=(',', ': '))
rf.write("\n]")

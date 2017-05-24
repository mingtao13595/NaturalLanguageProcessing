# coding: UTF-8
#!/usr/bin/env python

import MeCab
import re
import json

def morphologicalAnalysis(text, writeFile):
	m = MeCab.Tagger ("mecabrc")
	mp = m.parse (text)

	tmp_list = []
	tmp_word = ''
	for char in mp:
		if re.match('\t|\n|\,', char):
			char = re.sub(r'\s', '', char)
			char = re.sub(r'\,', '', char)
			tmp_list.append(tmp_word)
			tmp_word = ''
		tmp_word += char

	morpheme_list  = []
	morpheme_place = {}
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
			# ファイルへの書き込み
			json.dump(morpheme_place, writeFile, ensure_ascii=False, indent='\t', sort_keys=True, separators=(',', ': '))
			writeFile.write(",\n")

f = open('./file/neko.txt', 'r')
# 追記モードでファイルを開く
rf = open('./file/ex30_practice.json', 'a')
rf.write("[\n")
for line in f:
	morphologicalAnalysis(line, rf)
	# print(line)
json.dump({"end":"終"}, rf, ensure_ascii=False, indent='\t', sort_keys=True, separators=(',', ': '))
rf.write("\n]")

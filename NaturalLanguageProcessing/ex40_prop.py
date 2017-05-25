# coding: UTF-8
#!/usr/bin/env python

import MeCab
import CaboCha
import re
import json

def morphologicalAnalysis(text, writeFile):
	cabocha = CaboCha.Parser()
	mp = cabocha.parse(line).toString(CaboCha.FORMAT_LATTICE)

	tmp_list = []
	tmp_word = ''
	for char in mp:
		if re.match('\t|\n|\,', char):
			char = re.sub(r'\s', '', char)
			char = re.sub(r'\,', '', char)
			tmp_list.append(tmp_word)
			tmp_word = ''
		tmp_word += char

	print(tmp_list)

	print(len(tmp_list))

	# morpheme_list  = []
	# morpheme_place = {}
	# for i in range(len(tmp_list)):
	# 	if i % 10 == 0:
	# 		morpheme_place["surface"] = tmp_list[i]
	# 	elif i % 10 == 1:
	# 		morpheme_place["base"]    = tmp_list[i]
	# 	elif i % 10 == 2:
	# 		morpheme_place["pos"]     = tmp_list[i]
	# 	elif i % 10 == 3:
	# 		morpheme_place["pos1"]    = tmp_list[i]
	# 	elif i % 10 == 4:
	# 		morpheme_place["pos2"]    = tmp_list[i]
	# 	elif i % 10 == 5:
	# 		morpheme_place["pos3"]    = tmp_list[i]
	# 	elif i % 10 == 6:
	# 		morpheme_place["pos4"]    = tmp_list[i]
	# 	elif i % 10 == 7:
	# 		morpheme_place["pos5"]    = tmp_list[i]
	# 	elif i % 10 == 8:
	# 		morpheme_place["pos6"]    = tmp_list[i]
	# 	elif i % 10 == 9:
	# 		morpheme_place["pos7"]    = tmp_list[i]
	# 		# ファイルへの書き込み
	# 		json.dump(morpheme_place, writeFile, ensure_ascii=False, indent='\t', sort_keys=True, separators=(',', ': '))
	# 		writeFile.write(",\n")

f = open('./file/neko.txt', 'r')
# 追記モードでファイルを開く
rf = open('./file/ex40_practice.json', 'a')
rf.write("[\n")
for line in f:
	morphologicalAnalysis(line, rf)
	# print(line)
json.dump({"end":"終"}, rf, ensure_ascii=False, indent='\t', sort_keys=True, separators=(',', ': '))
rf.write("\n]")

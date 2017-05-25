# coding: UTF-8
#!/usr/bin/env python

import MeCab
import re
import json

def morphologicalAnalysis(text):
# def morphologicalAnalysis(text, writeFile):
	m  = MeCab.Tagger ("mecabrc")
	mp = m.parse (text)

	# print(mp)
	# print(len(mp))

	ws    = re.compile(" ")
	words = [word for word in ws.split(mp)]
	if words[-1] == u"\n":
		words = words[:-1]

	# エスケープシーケンスを無効化
	# word_toStr = str(words)
	# words_esc_sec = re.sub(r'\\', r'\\\\', word_toStr)
	# print(words_esc_sec)

	for char in words:
		char1 = re.sub(r'\t', ',', char)

	print(str(char1))
	print(len(char1))


	# print(words)
	# print(len(words))

	# tmp_list = []
	# tmp_word = ''
	#
	# # for char in words_esc_sec:
	# for char in words:
	# 	# print(char)
	# 	# print("\n")
	# 	if re.match(r'\\t|\\n|\,', char):
	# 		char = re.sub(r'\\t', '', char)
	# 		char = re.sub(r'\,', '', char)
	# 		tmp_list.append(tmp_word)
	# 		tmp_word = ''
	# 	tmp_word += char
	#
	# print(tmp_list)
	# print(len(tmp_list))


	# morpheme_list  = []
	# morpheme_place = {}
	# for i in range(len(tmp_list)):
	# 	if tmp_list[i] == "EOS"
	# 	elif i % 10 == 0:
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
# rf = open('./file/ex30_practice.json', 'a')
# rf.write("[\n")
for line in f:
	# morphologicalAnalysis(line, rf)
	morphologicalAnalysis(line)
	break
	# print(line)
# json.dump({"end":"終"}, rf, ensure_ascii=False, indent='\t', sort_keys=True, separators=(',', ': '))
# rf.write("\n]")

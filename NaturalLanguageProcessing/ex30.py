# coding: UTF-8
#!/usr/bin/env python

import MeCab
import re
import copy

def morphologicalAnalysis(text):
	m = MeCab.Tagger ("mecabrc")
	mp = m.parse (text)
	# mp = m.parse ("今日もしないとね")

	tmp_list = []
	tmp_word = ''
	for char in mp:
		if re.match('\t|\n|\,', char):
			char = re.sub(r'\s', '', char)
			char = re.sub(r'\,', '', char)
			tmp_list.append(tmp_word)
			tmp_word = ''
		tmp_word += char

	# 追記モードでファイルを開く
	rf = open('./file/ex30_practice.txt', 'a')
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
			# リストの値をコピー
			morpheme_place_copy = copy.deepcopy(morpheme_place)
			morpheme_list.append(morpheme_place_copy)
			# ファイルへの書き込み
			rf.write(
				"{'surface':" + morpheme_place_copy["surface"] + "," +
				"'base':" + morpheme_place_copy["base"] + "," +
				"'pos':" + morpheme_place_copy["pos"] + "," +
				"'pos1':" + morpheme_place_copy["pos1"] + "}\n"
			)
		# elif i % 10 == 5:
		# elif i % 10 == 6:
		# elif i % 10 == 7:
		# elif i % 10 == 8:
		# elif i % 10 == 9:

	# rf.close()

	# for line in morpheme_list:
	# 	print(line)

f = open('./file/neko.txt', 'r')

for line in f:
	morphologicalAnalysis(line)
	# print(line)

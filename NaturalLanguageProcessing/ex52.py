# coding: UTF-8
#!/usr/bin/env python

import re
import snowballstemmer
def morphologicalAnalysis(text):
	text_line = re.sub(r"\.|\;|\:|\?|\!", ' ', text)
	rowList = text_line.split(' ')
	return rowList

f = open('./file/nlp.txt', 'r')
# f = open('./file/english_test.txt', 'r')
worlds = []
stemmer = snowballstemmer.stemmer('english')

for line in f:
	worlds.extend(morphologicalAnalysis(line))

for word in worlds:
	stemming_word = stemmer.stemWord(word)
	print(stemming_word)

# coding: UTF-8
#!/usr/bin/env python

import MeCab
import re
import copy

f = open('./file/neko_morphologicalAnalysis.txt', 'r')

for line in f:
	dict_line = dict(line)
	print(dict_line)
	print(type(dict_line))
	break

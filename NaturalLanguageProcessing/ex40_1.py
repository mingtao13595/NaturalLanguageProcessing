# xmlを生成する
# coding: UTF-8
#!/usr/bin/env python

import MeCab
import CaboCha
import re
import json
import xmltodict

# xmlの変換処理
def textToXML(readFile, writeFile):
	f  = open(readFile, 'r')
	wf = open(writeFile, 'a')

	mt = CaboCha.Parser()
	for line in f:
		tree = mt.parse(line)
		wf.write(tree.toString(CaboCha.FORMAT_XML))

textToXML('./file/neko.txt', './file/ex40.xml')

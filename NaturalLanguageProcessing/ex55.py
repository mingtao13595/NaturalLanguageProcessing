# coding: UTF-8
#!/usr/bin/env python

import os
import subprocess
import xml.etree.ElementTree as ET

fname_parsed = 'nlp.txt.xml'
if not os.path.exists(fname_parsed):
	subprocess.run(
		'java -cp "/root/stanford-corenlp-full-2016-10-31/*"'
		' -Xmx2g'
		' edu.stanford.nlp.pipeline.StanfordCoreNLP'
		' -annotators tokenize,ssplit,pos,lemma,ner,parse,dcoref'
		' -file ' + './file/nlp.txt' + ' 2>parse.out',
		# shellで実行
		shell=True,
		# エラーチェックあり
		check=True
	)

# 解析結果のxmlをパース
root = ET.parse(fname_parsed)

# wordのみ取り出し
for token in root.iter('token'):
	if(token.findtext('NER') == 'PERSON'):
		print(token.findtext('word'))

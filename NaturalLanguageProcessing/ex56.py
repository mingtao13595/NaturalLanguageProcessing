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
		shell=True,
		check=True
	)

# xmlへパース
root = ET.parse(fname_parsed)

# 単語リストを生成
rep_dict = {}
for coreference in root.iterfind('./document/coreference/coreference'):
	# 代表参照の取得
	rep_text = coreference.findtext('./mention[@representative="true"]/text')
	# 辞書生成
	for mention in coreference.iterfind('./mention'):
		if(mention.get('representative', 'false') == 'false'):
			sent_id = int(mention.findtext('sentence'))
			start   = int(mention.findtext('start'))
			end     = int(mention.findtext('end'))
			if not (sent_id, start) in rep_dict:
				rep_dict[(sent_id, start)] = (end, rep_text)

# 本文の置換
for sentence in root.iterfind('./document/sentences/sentence'):
	sent_id  = int(sentence.get('id'))
	org_rest = 0

	# token列挙
	for token in sentence.iterfind('./tokens/token'):
		token_id = int(token.get('id'))

		# 置換対象を列挙
		if org_rest == 0 and (sent_id, token_id) in rep_dict:
			(end, rep_text) = rep_dict[(sent_id, token_id)]
			print('[' + rep_text + '] (', end='')
			org_rest = end - token_id
		print(token.findtext('word'), end='')

		# 置換の終わりの判定
		if(org_rest > 0):
			org_rest -= 1
			if(org_rest == 0):
				print(')', end='')
		print(' ', end='')

	# 改行
	print()

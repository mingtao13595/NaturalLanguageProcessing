# coding: utf-8
#!/usr/bin/env python

import os
import subprocess
import xml.etree.ElementTree as ET
import re

fname_parsed = 'nlp.txt.xml'
pattern = re.compile(r'''
	^
	\(
		(.*?)
		\s
		(.*)
	\)
	$
	''', re.VERBOSE + re.DOTALL)

def ParseAndExtractNP(str, list_np):
	# タグと内容を抽出
	match = pattern.match(str)
	tag   = match.group(1)
	value = match.group(2)

	# カッコの深さ
	depth = 0
	# 切り出し中の文字列
	chunk = ''
	words = []
	for c in value:
		if c == '(':
			chunk += c
			# 深くなった
			depth += 1
		elif c == ')':
			chunk += c
			# 浅くなった
			depth -= 1
			if depth == 0:
				words.append(ParseAndExtractNP(chunk, list_np))
				chunk = ''
		else:
			# カッコでくくられていない部分の空白は無視
			if not (depth == 0 and c == ' '):
				chunk += c
	# 最後の単語を追加
	if chunk != '':
		words.append(chunk)
	# 空白区切りに整形
	result = ' '.join(words)
	# NPならlist_npに追加
	if tag == 'NP':
		list_np.append(result)
	return result

# nlp.txtを解析
if not os.path.exists(fname_parsed):
	# StanfordCoreNLP実行、標準エラーはparse.outへ出力
	subprocess.run(
		'java -cp "/root/stanford-corenlp-full-2016-10-31/*"'
		' -Xmx2g'
		' edu.stanford.nlp.pipeline.StanfordCoreNLP'
		' -annotators tokenize,ssplit,pos,lemma,ner,parse,dcoref'
		' -file ' + './file/nlp.txt' + ' 2>parse.out',
		shell=True,
		check=True
	)

# 解析結果のxmlをパース
root = ET.parse(fname_parsed)

# sentence列挙、1文ずつ処理
for parse in root.iterfind('./document/sentences/sentence/parse'):
	result = []
	ParseAndExtractNP(parse.text.strip(), result)
print(*result, sep='\n')

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
	match = pattern.match(str)
	tag   = match.group(1)
	value = match.group(2)

	depth = 0
	chunk = ''
	words = []
	for c in value:
		if c == '(':
			chunk += c
			depth += 1
		elif c == ')':
			chunk += c
			depth -= 1
			if depth == 0:
				words.append(ParseAndExtractNP(chunk, list_np))
				chunk = ''
		else:
			if not (depth == 0 and c == ' '):
				chunk += c
	if chunk != '':
		words.append(chunk)
	result = ' '.join(words)
	if tag == 'NP':
		list_np.append(result)
	return result

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

root = ET.parse(fname_parsed)

for parse in root.iterfind('./document/sentences/sentence/parse'):
	result = []
	ParseAndExtractNP(parse.text.strip(), result)
print(*result, sep='\n')

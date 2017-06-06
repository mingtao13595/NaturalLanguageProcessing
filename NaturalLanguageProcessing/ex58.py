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

# sentence列挙、1文ずつ処理
for sentence in root.iterfind('./document/sentences/sentence'):
	# sentenceのid
	sent_id = int(sentence.get('id'))
	# それぞれの語の辞書を作成_{述語のidx, 述語のtext}
	dict_pred  = {}
	# それぞれの語の辞書を作成_{述語のidx, 述語とnsubj関係の子のtext（＝主語）}
	dict_nsubj = {}
	# それぞれの語の辞書を作成_{述語のidx, 述語とdobj関係の子のtext（＝目的語）}
	dict_dobj  = {}
	# dependencies列挙
	for dep in sentence.iterfind('./dependencies[@type="collapsed-dependencies"]/dep'):
		# 関係チェック
		dep_type = dep.get('type')
		# 単語の属性を確認する
		if dep_type == 'nsubj' or dep_type == 'dobj':
			# 述語の辞書に追加
			govr           = dep.find('./governor')
			# 結果のインデックス
			idx            = govr.get('idx')
			# 重複するが無害なのでチェックは省略
			dict_pred[idx] = govr.text
			# 主語or目的語の辞書に追加
			if dep_type == 'nsubj':
				dict_nsubj[idx] = dep.find('./dependent').text
			else:
				dict_dobj[idx]  = dep.find('./dependent').text
	# 述語を列挙、主語と目的語の両方を持つもののみ出力
	for idx, pred in sorted(dict_pred.items(), key=lambda x: x[0]):
		nsubj = dict_nsubj.get(idx)
		dobj  = dict_dobj.get(idx)
		if nsubj is not None and dobj is not None:
			print('{}\t{}\t{}'.format(nsubj, pred, dobj))

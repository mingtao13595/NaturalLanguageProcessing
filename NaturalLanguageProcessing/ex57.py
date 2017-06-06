# coding: UTF-8
#!/usr/bin/env python

import os
import subprocess
import pydot_ng as pydot
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
	sent_id = int(sentence.get('id'))
	edges   = []

	# dependencies列挙
	for dep in sentence.iterfind(
		'./dependencies[@type="collapsed-dependencies"]/dep'
	):
		# 句読点はスキップ
		if dep.get('type') != 'punct':
			# governor、dependent取得、edgesに追加
			govr = dep.find('./governor')
			dept = dep.find('./dependent')
			edges.append(
				((govr.get('idx'), govr.text), (dept.get('idx'), dept.text))
			)

	# 描画
	if len(edges) > 0:
		graph = pydot.Dot(graph_type='digraph')
		for edge in edges:
			id1    = str(edge[0][0])
			label1 = str(edge[0][1])
			id2    = str(edge[1][0])
			label2 = str(edge[1][1])
			# ノード追加
			graph.add_node(pydot.Node(id1, label=label1))
			graph.add_node(pydot.Node(id2, label=label2))
			# エッジ追加
			graph.add_edge(pydot.Edge(id1, id2))
		graph.write_png('./file/{}.png'.format(sent_id))

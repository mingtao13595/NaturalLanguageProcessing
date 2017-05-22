# coding: UTF-8
#!/usr/bin/env python
import MeCab
m = MeCab.Tagger ("-Ochasen")
print (m.parse ("今日もしないとね"))

# f = open('./file/neko.txt', 'r')
# mt = MeCab.Tagger("-Ochasen")
# mt.parse('')
# node = mt.parseToNode(f)
# while node:
# 	print (node.surface, node.feature)
# 	node = node.next

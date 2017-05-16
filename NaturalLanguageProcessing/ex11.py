# coding: UTF-8
#!/usr/bin/env python
f = open('./file/hightemp.txt', 'r')
row_length = sum(1 for line in f)
f.close()
f = open('./file/hightemp.txt', 'r')
for line in f:
	line_tabToSpace = line.replace('\t', ' ')
	print(line_tabToSpace)
f.close()

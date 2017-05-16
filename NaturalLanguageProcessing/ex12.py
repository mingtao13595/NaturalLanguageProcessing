# coding: UTF-8
#!/usr/bin/env python
f   = open('./file/hightemp.txt', 'r')
wf1 = open('./file/col1.txt', 'w')
wf2 = open('./file/col2.txt', 'w')
for line in f:
	lineList = line[:-1].split('\t')
	wf1.write(lineList[1]+"\n")
	wf2.write(lineList[2]+"\n")
wf1.close()
wf2.close()
f.close()

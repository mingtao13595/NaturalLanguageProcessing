# coding: UTF-8
#!/usr/bin/env python
union_array = {
	'col1' : [],
	'col2' : []
}

f1 = open('./file/col1.txt', 'r')
for line in f1:
	lineList = line[:-1]
	union_array['col1'].append(lineList)
f1.close()

f2 = open('./file/col2.txt', 'r')
for line in f2:
	lineList = line[:-1]
	union_array['col2'].append(lineList)
f2.close()

wf = open('./file/ex13_result.txt', 'w')
# print(len(union_array['col1']))
for count in range(len(union_array['col1'])):
	wf.write(union_array['col1'][count]+"\t"+union_array['col2'][count]+"\n")
wf.close()

# coding: UTF-8
#!/usr/bin/env python
f = open('./file/hightemp.txt', 'r')
row_length = sum(1 for line in f)

print (row_length)

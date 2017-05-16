N = 7
f   = open('./file/hightemp.txt', 'r')
fileList   = []
for line in f:
	lineList = line[:-1]
	fileList.append(lineList)
f.close()

for i in range(N):
	print(fileList[i])

# print(fileList)

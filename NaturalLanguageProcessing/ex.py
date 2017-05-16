N=7
f   = open('./file/hightemp.txt', 'r')
fileList   = []
for line in f:
	lineList = line[:-1]
	fileList.append(lineList)
f.close()

# print(round(len(fileList)/N))
split = round(len(fileList)/N)
print(split)

for i in range(len(fileList)):
	if float(i) % float(split) == 0.0:
		print("-----------------------------")
	print(fileList[len(fileList)-1-i])

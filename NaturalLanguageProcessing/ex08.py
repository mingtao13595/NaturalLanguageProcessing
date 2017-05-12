#coding: UTF-8
import re

def char_list(sentence):
	elementList = sentence.strip()
	wordList = []
	for i in range(len(elementList)):
		wordList.append(elementList[i])
		if i+1 == len(elementList):
			return wordList

def cipher(charcter):
	output   = ""
	pattern  = re.compile(r'^[a-z]+$')
	charList = char_list(charcter)
	for i in charList:
		matchObj = pattern.match(i)
		if matchObj != None:
			str = 219 - ord(i)
			output += chr(str)
		else:
			output += i
	return output

print(cipher('PpaP I have a pen'))

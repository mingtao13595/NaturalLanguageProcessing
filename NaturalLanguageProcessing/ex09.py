#coding: UTF-8
import random

def word_list(sentence):
	wordList = sentence.split(" ")
	return wordList

def char_list(elementList):
	charList = []
	for i in range(len(elementList)):
		charList.append(elementList[i])
		if i+1 == len(elementList):
			return charList

def randomOp(charList):
	result_random_line_up_list = []
	result_random_line_up_list.append(charList[0])
	tmp_char = charList[len(charList)-1]
	charList.pop(0)
	charList.pop(len(charList)-1)
	random.shuffle(charList)
	result_random_line_up_list.extend(charList)
	result_random_line_up_list.append(tmp_char)
	return result_random_line_up_list

def typoglycemia(charcter):
	wordList   = word_list(charcter)
	resultList = []
	for i in wordList:
		if len(i) < 5:
			resultList.append(i)
		else:
			charList = char_list(i)
			randomResult = randomOp(charList)
			randomWord = "".join(randomResult)
			resultList.append(randomWord)
	resultSentence = " ".join(resultList)
	return resultSentence

print(typoglycemia('I couldn\'t believe that I could actually understand what I was reading : the phenomenal power of the human mind .'))

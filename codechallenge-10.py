'''
Date: 12/20/2018

Problem description:
====================
This problem was asked by Microsoft.

Given a dictionary of words and a string made up of those words (no spaces), 
return the original sentence in a list. If there is more than one possible 
reconstruction, return any of them. If there is no possible reconstruction, then return null.

For example, given the set of words 'quick', 'brown', 'the', 'fox', and the 
string "thequickbrownfox", you should return ['the', 'quick', 'brown', 'fox'].

Given the set of words 'bed', 'bath', 'bedbath', 'and', 'beyond', and the 
string "bedbathandbeyond", return either ['bed', 'bath', 'and', 'beyond] 
or ['bedbath', 'and', 'beyond'].



Assumption:
The first sentence threw me off a bit because I was thinking python.  
Dictionary and list in the same sentence makes me deduce it is a given list of words.

The words are ASCII format
But will look into utf-8 implementation later.
'''
import collections

dictRetString = {}

def findWord(wordsList, wordString):
	# edge case
	if len(wordsList) == 0 or len(wordString) == 0:
		return None

	for word in wordsList:
		if word in wordString:
			pos = wordString.find(word)
			dictRetString[int(pos)] = str(word)

	# sort the keys 
	sortedDList = collections.OrderedDict(sorted(dictRetString.items()))
	return list(sortedDList.values())



def test_code():
	# test1:
	dictRetString = {}
	wList =[ 'quick', 'brown', 'the', 'fox' ] 
	wStr = "thequickbrownfox"
	expected = ['the', 'quick', 'brown', 'fox']
	assert findWord(wList, wStr) == expected

	#test2:  ** I know this test will fail...  will update fix here soon **
	dictRetString = {}
	words = ['bed', 'bath', 'bedbath', 'and', 'beyond'] 
	string = "bedbathandbeyond"
	expected = ['bed', 'bath', 'and', 'beyond'] 
	assert findWord(words, string) == expected


if __name__ == "__main__":
	dictRetString = {}
	wList =[ 'quick', 'brown', 'the', 'fox' ] 
	wStr = "thequickbrownfox"
	expected = ['the', 'quick', 'brown', 'fox']
	print("Given\nA word list: {} and a string: {}".format(wList, wStr))
	print("Matches are found in: {}\n".format(findWord(wList, wStr)))

	dictRetString = {}
	words = ['bed', 'bath', 'bedbath', 'and', 'beyond'] 
	string = "bedbathandbeyond"
	expected = ['bed', 'bath', 'and', 'beyond'] 
	print("Given\nA word list: {} and a string: {}".format(words, string))
	print("Matches are found in: {}\n".format(findWord(words, string)))


'''
Run-time output:
===============
$ python codechallenge-10.py
Given
A word list: ['quick', 'brown', 'the', 'fox'] and a string: thequickbrownfox
Matches are found in: ['the', 'quick', 'brown', 'fox']

Given
A word list: ['bed', 'bath', 'bedbath', 'and', 'beyond'] and a string: bedbathandbeyond
Matches are found in: ['bedbath', 'bath', 'and', 'beyond']

'''

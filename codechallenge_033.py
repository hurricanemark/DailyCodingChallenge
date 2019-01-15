'''
Date: 01/15/2019

Problem description:
====================
This problem was asked by Facebook.

Given a array of numbers representing the stock prices of a company in 
chronological order, write a function that calculates the maximum profit 
you could have made from buying and selling that stock once. You must 
buy before you can sell it.

For example, given [9, 11, 8, 5, 7, 10], you should return 5, since you 
could buy the stock at 5 dollars and sell it at 10 dollars.


Algorithm:
=========
Input: An array of integers
Output: An integer

Pseudo code:

1.  Check for valid input
2.  Find the min value and its index from the array.  This will be the buy item 
	Since we can't go back, the new array will start from this new index
3.  From the new array, find the max value and its index.  This will be the sell item.  
4.  Return the difference between the values from the above indices  

No looping through the list.
This is why I love Python!

'''


#
# O(2) comparision
#
def profit(price_list=[]):
	if len(price_list) == 0:
		return 0

	# buy low
	buyAtIdx = price_list.index(min(price_list))
	buyPrice = price_list[buyAtIdx]

	new_price_list = price_list[buyAtIdx:]

	# sell high
	sellPrice = max(new_price_list)
	sellAtIdx = price_list.index(sellPrice)

	#profit
	profit = sellPrice - buyPrice

	# verbish
	print("For maximum profit we buy at {} and sell at {} for the profit of {}.".format(buyPrice, sellPrice, profit))
	
	# return profit
	return int(profit)

#
# unittest
#	
def test_profit():
	A = [19, 157, 163, 99, 200, 215, 189, 201, 205, 199]
	assert profit(A) > 0
	assert profit(A) == 196

#
# client program 
#
def main():
	stock_prices = [9, 11, 8, 5, 7, 10]
	print("Test1:\nGiven progressing stock prices {}".format('->'.join(str(i) for i in stock_prices)))
	profit(stock_prices)

if __name__ == '__main__':
	main()

'''
Run-time output:
===============
(DailyCodingChallenge-wC3ocw3s) markn@raspberrypi3:~/devel/py-src/DailyCodingChallenge $ python codechallenge_033.py
Test1:
Given progressing stock prices 9->11->8->5->7->10
For maximum profit we buy at 5 and sell at 10 for the profit of 5.
(DailyCodingChallenge-wC3ocw3s) markn@raspberrypi3:~/devel/py-src/DailyCodingChallenge $ pytest codechallenge_033.py
=============================== test session starts ===============================
platform linux2 -- Python 2.7.13, pytest-3.6.3, py-1.5.4, pluggy-0.6.0
rootdir: /home/markn/devel/py-src/DailyCodingChallenge, inifile:
collected 1 item

codechallenge_033.py .                                                      [100%]

============================ 1 passed in 0.12 seconds =============================
'''

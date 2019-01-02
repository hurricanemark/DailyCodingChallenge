'''
Date: 12/29/2018

Problem description:
===================
This problem was asked by Jane Street.

Suppose you are given a table of currency exchange rates, represented as a 2D array. 
Determine whether there is a possible arbitrage: that is, whether there is some sequence 
of trades you can make, starting with some amount A of any currency, so that you can 
end up with some amount greater than A of that currency.

There are no transaction costs and you can trade fractional quantities.


Some research:
=============
Arbitrage involves three immediate transactions of buy low sell high.
For example, we use 2 US dollars to buy 1 British pound sterling, 
then use that pound to buy 1.50 euros, and then use the l.50 euros 
to buy $2.50. By trading this way we have gained $0.50
In actuality, arbitrage takes advantage of market inefficiency(delay in infomation 
sharing) to trade for fractional gain


Below is the actual currency exchange rate table on 12-31-2018
US Dollar 		1.00 USD 	inv. 1.00 USD
---------    		--------    -------------
Euro 			0.870903 	1.148233
British Pound 		0.783992 	1.275523
Indian Rupee 		69.605725 	0.014367
Australian Dollar 	1.420549 	0.703953
Canadian Dollar 	1.363172 	0.733583
Singapore Dollar 	1.362844 	0.733760
Swiss Franc 		0.983397 	1.016883
Malaysian Ringgit 	4.132583 	0.241979
Japanese Yen 		109.558545 	0.009128
Chinese Renminbi 	6.874934 	0.145456



Given:
USCurrencyEquivalent = {
				"Euro": 0.870903,
				"British Pound": 0.783992,
				"Indian Rupee": 69.605725,
				"Australian Dollar": 1.420549,
				"Canadian Dollar": 1.363172,
				"Singapore Dollar": 1.362844,
				"Swiss Franc": 0.983397,
				"Malaysian Ringgit": 4.132583,
				"Japanese Yen": 109.558545,
				"Chinese Renminbi": 6.874934
				}
Then figure out the inversion rate, 
# e.g. 1 Euro = 1.148233 US
USInversionRate = {
				"Euro": 1.148233,
                "British Pound": 1.275523,
                "Indian Rupee": 0.014367,
                "Australian Dollar": 0.703953,
                "Canadian Dollar": 0.733583,
                "Singapore Dollar": 0.733760,
                "Swiss Franc": 1.016883,
                "Malaysian Ringgit": 0.241979,
                "Japanese Yen": 0.009128,
                "Chinese Renminbi": 0.145456
			}

The best marginal gain is 1 * (lowest inversion rate / highest inversion rate)
e.g. 1US * (0.009128Yen/1.275523Pound) = 0.007156280208196952US
If we invest 1000US buying Pound then Yen then back to US dollars, we gain 1000 * 0.007156280208196952 = 7.156$


Algorithm:
=========
Input: A dictionary of USCurrencyEquivalent, and an investment number in US dollars
Ouput: Gain in decimal value of US dollars
Pseudo code:
1.  Check for valid input
2.  Convert dictionary into inversion hash table
3.  Find the highest ratio in the hash table. i.e. lowest/highest
4.  Output the InvestAmount * (ratio)

'''


def inversionRatio(USCurrencyEquivalent={}):
	for k in USCurrencyEquivalent:
		#print (k, 1/USCurrencyEquivalent[k])		
 		USCurrencyEquivalent[k] = 1 / USCurrencyEquivalent[k]
	return USCurrencyEquivalent

def gainArbitrage(USCurrencyEquivalent, AmountUSD):
	inversionHash = inversionRatio(USCurrencyEquivalent)

	# step1
	maxrate = max([inversionHash[k] for k in inversionHash])
	XAmount = AmountUSD/maxrate
	XCurrencyName = [k for k,v in inversionHash.items() if v == maxrate]
	print("Step1: Trade {} USD for {} {}".format(AmountUSD, XAmount, str(XCurrencyName[0])))

	# step2
	minrate = min([inversionHash[k] for k in inversionHash])
	YAmount = XAmount/minrate	
	YCurrencyName = [k for k,v in inversionHash.items() if v == minrate]
	print("Step2: Trade {} {} for {}{}".format(XAmount, str(XCurrencyName[0]), YAmount, str(YCurrencyName[0])))

	# step3
	ZAmount = AmountUSD + AmountUSD *(minrate/maxrate)
	print("Step3: Trade {} {} back to {} USD".format(YAmount, str(YCurrencyName[0]), ZAmount)) 

	return AmountUSD * (minrate/maxrate)


def test_code():
    InvestAmount = 1000000
    USCurrencyEquivalent = {
                "Euro": 0.870903,
                "British Pound": 0.783992,
                "Indian Rupee": 69.605725,
                "Australian Dollar": 1.420549,
                "Canadian Dollar": 1.363172,
                "Singapore Dollar": 1.362844,
                "Swiss Franc": 0.983397,
                "Malaysian Ringgit": 4.132583,
                "Japanese Yen": 109.558545,
                "Chinese Renminbi": 6.874934 }
    assert gainArbitrage(USCurrencyEquivalent, InvestAmount) == 7155.91832658968 

if __name__ == '__main__':
	Amount = 1000000 # US dollars
	USCurrencyEquivalent = {
                "Euro": 0.870903,
                "British Pound": 0.783992,
                "Indian Rupee": 69.605725,
                "Australian Dollar": 1.420549,
                "Canadian Dollar": 1.363172,
                "Singapore Dollar": 1.362844,
                "Swiss Franc": 0.983397,
                "Malaysian Ringgit": 4.132583,
                "Japanese Yen": 109.558545,
                "Chinese Renminbi": 6.874934
                }
	print("Gain from arbitrage trades: {} USD".format(gainArbitrage(USCurrencyEquivalent, Amount)))



'''
Run-time output:
===============
Step1: Trade 1000 USD for 783.992 British Pound
Step2: Trade 783.992 British Pound for 85893.0228116Japanese Yen
Step3: Trade 85893.0228116 Japanese Yen back to 1007.15591833 USD
Gain from arbitrage trades: 7.15591832659 USD
'''


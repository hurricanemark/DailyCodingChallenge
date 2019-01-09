'''
Date: 01/09/2019

Problem descriptions:
====================
This problem was asked by Facebook.
Given an unordered list of flights taken by someone, each represented as (origin, destination) pairs, and a starting airport, compute the person's itinerary. If no such itinerary exists, return null. If there are multiple possible itineraries, return the lexicographically smallest one. All flights must be used in the itinerary.
For example, given the list of flights [('SFO', 'HKO'), ('YYZ', 'SFO'), ('YUL', 'YYZ'), ('HKO', 'ORD')] and starting airport 'YUL', you should return the list ['YUL', 'YYZ', 'SFO', 'HKO', 'ORD'].
Given the list of flights [('SFO', 'COM'), ('COM', 'YYZ')] and starting airport 'COM', you should return null.
Given the list of flights [('A', 'B'), ('A', 'C'), ('B', 'C'), ('C', 'A')] and starting airport 'A', you should return the list ['A', 'B', 'C', 'A', 'C'] even though ['A', 'C', 'A', 'B', 'C'] is also a valid itinerary. However, the first one is lexicographically smaller.


Algorithm:
=========
Input: An array of tuples, and a string (representing available flights & starting airport)
Output: An array of tuples (representing connecting flights)
Psuedo code:
1.  Check for valid input
2.  Initialize an empty itinerary list. Assign departure points from the flight list
4.  determine the destination point of the given starting airport.  Append start,end points to the Itnerary list.
5.  determine the arrival airport from the above destination, next start point equals to arrival airport.
6.  keep doing step4,5 until the available flight list is exhausted
7.  return the itineray list

'''

#
# return list of connecting flights
#
def getItin(FLIGHTS, START):
	ITIN = []
	try:
		for idx,val in enumerate(FLIGHTS):
			DEP=[(i,d[0]) for i,d in enumerate(iter(FLIGHTS))]
			endidx = [list(i)[0] for i in DEP if list(i)[1] == START][-1]
			ITIN.append(FLIGHTS[endidx])
			START = list(ITIN[-1])[1]
	except IndexError:
		pass
	return ITIN


def test_getItin():
	flights=[('SFO', 'HKO'), ('YYZ', 'SFO'), ('YUL', 'YYZ'), ('HKO', 'ORD')]
	start='YUL'
	assert getItin(flights, start) == [('YUL', 'YYZ'), ('YYZ', 'SFO'), ('SFO', 'HKO'), ('HKO', 'ORD')]
 
	start='ORD'
	assert getItin(flights, start) == []

def main():
	flights=[('SFO', 'HKO'), ('YYZ', 'SFO'), ('YUL', 'YYZ'), ('HKO', 'ORD')]
	start='YUL'
	itinerary = getItin(flights, start)
	if len(itinerary) > 0:
		print("Test1:\nGiven the starting airport is {} and available flights [{}]\nPossible itinerary is [{}]".format(start, ', '.join(str(f) for f in flights), ', '.join(str(f) for f in itinerary)))
		print()

	start='SFO'
	itinerary = getItin(flights, start)
	if len(itinerary) > 0:
		print("Test2:\nGiven the starting airport is {} and available flights [{}]\nPossible itinerary is [{}]".format(start, ', '.join(str(f) for f in flights), ', '.join(str(f) for f in itinerary)))
		print()

	start='ORD'
	itinerary = getItin(flights, start)
	if len(itinerary) > 0:
		print("Test3:\nGiven the starting airport is {} and available flights [{}]\nPossible itinerary is [{}]".format(start, ', '.join(str(f) for f in flights), ', '.join(str(f) for f in itinerary)))
		print()
	else:
		print("Test3:\nGiven the starting airport is {} and available flights [{}]\nPossible itinerary is [{}]".format(start, ', '.join(str(f) for f in flights), 'None'))


if __name__ == '__main__':
	main()


'''
Run-time output:
===============
(DailyCodingChallenge-wC3ocw3s) markn@raspberrypi3:~/devel/py-src/DailyCodingChallenge $ python codechallenge_027.py
Test1:
Given the starting airport is YUL and available flights [('SFO', 'HKO'), ('YYZ', 'SFO'), ('YUL', 'YYZ'), ('HKO', 'ORD')]
Possible itinerary is [('YUL', 'YYZ'), ('YYZ', 'SFO'), ('SFO', 'HKO'), ('HKO', 'ORD')]

Test2:
Given the starting airport is SFO and available flights [('SFO', 'HKO'), ('YYZ', 'SFO'), ('YUL', 'YYZ'), ('HKO', 'ORD')]
Possible itinerary is [('SFO', 'HKO'), ('HKO', 'ORD')]

Test3:
Given the starting airport is ORD and available flights [('SFO', 'HKO'), ('YYZ', 'SFO'), ('YUL', 'YYZ'), ('HKO', 'ORD')]
Possible itinerary is [None]

(DailyCodingChallenge-wC3ocw3s) markn@raspberrypi3:~/devel/py-src/DailyCodingChallenge $ pytest codechallenge_027.py
============================ test session starts ============================
platform linux2 -- Python 2.7.13, pytest-3.6.3, py-1.5.4, pluggy-0.6.0
rootdir: /home/markn/devel/py-src/DailyCodingChallenge, inifile:
collected 1 item

codechallenge_027.py .                                                [100%]

========================= 1 passed in 0.08 seconds ==========================

'''

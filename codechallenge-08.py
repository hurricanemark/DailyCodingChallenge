'''
Date: 12/20/2018

Problem description:
====================
This problem was asked by Snapchat.

Given an array of time intervals (start, end) for classroom lectures 
(possibly overlapping), find the minimum number of rooms required.



For example, given [(30, 75), (0, 50), (60, 150)], you should return 2.


  (room)
    ^
    |
3   -
    |
2   -**************  ***************************
    |
1   -       **************
    |
0 ----.--.--.--.--.--.--.--.--.--.--.--.--.--.--.--.--.--.--.--> (time)
    | 10 20 30 40 50 60 70 80 90   110   130      160 

Base on the above graph of distribution, the return value is 2 rooms.


Psuedo code:
===========
1.  Edge cases-- check empty array, start > end time
2.  Convert the array of tuples into a hash table (dict).
3.  Copy the keys into start-time list, values into end-time list
4.  Loop the length of one list, if subsequent start-time is less than 
    previous end-time then overlap occurs, get another room.
Note, it is easier to hash the array by converting it into a dictionary.
Also, no time gap in between back-to-back schedules is considered in this implementation.
'''

import random, time
def reserveRooms(schedList):
	# edge cases
	if len(schedList) == 0:
		return 0 

	# convert list into hash table
	dSchedList = dict(schedList)
	rooms = 0
	stimes = list(dSchedList.keys())
	etimes = list(dSchedList.values())	

	# loop over the list and apply logic
	for i in range(len(stimes)-1):
		if stimes[i+1] > stimes[i]:
			rooms+=1	

		if etimes[i] < stimes[i+1]:
			rooms+=1

	return rooms

def genRandomSchedule(slots):
	sched = [(int(100*random.random()), int(100*random.random())) \
		for i in range(slots)]
	sched.sort(reverse=True)
	dsched = dict(sched)
	dsched = {key:val+key for (key, val) in dsched.items()}

	# Since random generator is used for pass-in schedList, 
	# check if endTime is less than startTime.
	# if found we ignore the particular item by removing it from the dictionary
	for start, end in dsched.items():
		if start > end:
			del dsched[start]
			#print("Throw away time slot: {}".format(start,end))
	sched = list(dsched.items())
	return sched

def test_code():
	schedtime = [(30, 75), (0, 50), (60, 150)]
	begin = time.time()
	assert reserveRooms(schedtime) == 2
	end = time.time()
	print("Elapsed time: {}".format(end-begin))

if __name__ == "__main__":
	# test base case given in the problem
	schedtime = [(30, 75), (0, 50), (60, 150)]
	print("Given a schedule: {}".format(schedtime))
	begin = time.time()
	print ("Number of required room(s): {}".format(reserveRooms(schedtime)))
	end = time.time()
	print("Elapsed time: {}\n".format(end-begin))

	# test using random generator
	schedtime = genRandomSchedule(7)
	print("Random generated schedule: {}".format(schedtime))
	begin = time.time()
	print ("Number of required room(s): {}".format(reserveRooms(schedtime)))
	end = time.time()
	print("Elapsed time: {}\n".format(end-begin))

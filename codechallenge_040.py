'''
Date: 01/27/2019

Problem description:
===================
This problem was asked by Google.
Implement a file syncing algorithm for two computers over a low-bandwidth network. 
What if we know the files in the two computers are mostly the same?


Forethought:
============
(*) Let's assume that there is a master and a slave.  File tree is synchronized from 
master to slave.  Otherwise, we will spend much longer time trying to implement a file 
merginng algorithm that could ventually open up to a lengthy revision control program.  

(**)  Let's assume also that this is not a monitorin program.  Hence, we are not doing 
the metadata collection on file changes.

Algorithm:
==========
Input: Two file tree structures
Output: Message....

Psuedo code:
1.  Sync the two system clocks
2.  Traverse the file trees comparing file checksums, or timestamps
3.  Perform file copy/delete, etc.


'''

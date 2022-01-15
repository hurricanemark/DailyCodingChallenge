'''
Date: 01/05/2020

This problem was asked by Google.
Problem description:
====================
Suppose we represent our file system by a string in the following manner:
The string "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext" represents:

dir
    subdir1
    subdir2
        file.ext
        
The directory dir contains an empty sub-directory subdir1 and a sub-directory subdir2 containing a file file.ext.
The string "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext" represents:

`print("dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext")`

dir
    subdir1
        file1.ext
        subsubdir1
    subdir2
        subsubdir2
            file2.ext
            
The directory dir contains two sub-directories subdir1 and subdir2. subdir1 contains a file file1.ext and an empty second-level sub-directory subsubdir1. subdir2 contains a second-level sub-directory subsubdir2 containing a file file2.ext.
We are interested in finding the longest (number of characters) absolute path to a file within our file system. For example, in the second example above, the longest absolute path is "dir/subdir2/subsubdir2/file2.ext", and its length is 32 (not including the double quotes).
Given a string representing the file system in the above format, return the length of the longest absolute path to a file in the abstracted file system. If there is no file in the system, return 0.

Note:
=====
The name of a file contains at least a period and an extension.
The name of a directory or sub-directory will not contain a period.

Algorithm:
==========
1.  Validate input
2.  Tokenize the input string
3.  Concatenate the tokens into a list of strings, each string representing an absolute path will end with at least a period and an extension.
4.  Compare the length of each string to the longest length found so far.
'''
import re as regexp
def longest_absolute_path(input_string):
    if not input_string:
        raise Exception("Empty input string")
    
    # tokenize the input string
    tokens = input_string.split('\n')
    
    # concatenate the tokens into a list of strings, each string representing an absolute path will end with at least a period and an extension.
    paths = []
    for token in tokens:
        if token.endswith('.'):
            paths.append(token)
        else:
            paths.append(token)

    arr = ['dir', '\tsubdir1', '\t\tfile1.ext']
    print(count_tabs(arr))
    
    tmpPaths = []
    [print(x) for x in paths if x.startswith('\t')]
    print('-----------------')
    [ tmpPaths.append(regexp.sub(r"[\n\t\s]*", "", x)) for x in paths] # remove leading tabs    
    print(tmpPaths)
    
    # compare the length of each string to the longest length found so far.
    longest_length = 0
    for path in paths:
        if len(path) > longest_length:
            longest_length = len(path)
            
    
    return longest_length



def count_tabs(arr):
    count_tab=0
    count_space=0
    count_newline=0
    if type(arr) == list:
        print(arr)
        for x in arr:
            if x.startswith('\t'):
                x.count('\t', 0, len(x)):
                    count_tab += x.count('\t', 0, len(x))
            elif x.startswith(' '):
                count_space += 1
            elif x.startswith('\n'):
                count_newline += 1

    print("How many Tabs are present in the array? ", count_tab)
    print("How many Spaces are present in the array? ", count_space)
    print("How many Newlines are present in the array? ", count_newline)

if __name__ == '__main__':
    print(longest_absolute_path("dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"))
    
'''
Date: 05/04/2022

Problem description:
====================
This problem was asked by Nest.

Create a basic sentence checker that takes in a stream of characters and determines 
whether they form valid sentences. If a sentence is valid, the program should print it out.

We can consider a sentence valid if it conforms to the following rules:

The sentence must start with a capital letter, followed by a lowercase letter or a space.
All other characters must be lowercase letters, separators (,,;,:) or terminal marks (.,?,!,‽).
There must be a single space between each word.
The sentence must end with a terminal mark immediately following a word.

Algorithm:
==========
1.  Validate input
2.  Check for single space between each word
3.  Check for terminal mark at the end of the stream
4.  Split the stream into array of characters.  Traverse the array checking for capitalized 1st letter, alphanumeric, separators.
5.  Return False if conditions not met, else print the sentence.
'''

def check_sentence(stream):
    # check for single space between each word
    if len(stream.split('  ')) > 1:
        return False
    # check if the sentence ends with a terminal mark
    if list(stream)[-1] not in ['.','!','?','‽']:
        return False
    
    # Traverse the stream and check for the followings:
    for i,c in enumerate(list(stream)):
        # is first c a capital letter?
        if i == 0:
            if c.isalnum() and c.isupper():
                continue
            else:
                print('debug: i=',i, 'c=',c)
                return False
        else: # i > 0
            if c.isspace():
                if (list(stream)[i+1].isspace()):
                    print('debug: i=',i, 'c=',c)
                    return False
            
            elif (c.isalnum() and c.islower()) or (c in [',',';',':','.']):
                continue
            else:
                print('debug: i=',i, 'c=',c)
                return False
    print(stream)
    return True


#
# main driver
#
def main():
    sentence = 'The quick brown fox jumps over the lazy dog.'
    print(check_sentence(sentence))
    not_sentence = 'ohhh,  it  is not a sentence'
    print(check_sentence(not_sentence))
    
if __name__ == '__main__':
    main()
        
'''
Question 14
Level 2

Question:
Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
Suppose the following input is supplied to the program:
Hello world!
Then, the output should be:
UPPER CASE 1
LOWER CASE 9

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.


'''


def find_upper_lower_leeters(str):
    dict={'upper':0,'lower':0}
    for s in str:
        if s.isalpha():
            if s.islower():
                dict['lower']+=1
            elif s.isupper():
                dict['upper'] += 1
    print 'UPEER CASE', dict['upper']
    print 'LOWER CASE', dict['lower']


str=raw_input()
find_upper_lower_leeters(str)

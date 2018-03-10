'''
Question 13
Level 2

Question:
Write a program that accepts a sentence and calculate the number of letters and digits.
Suppose the following input is supplied to the program:
hello world! 123
Then, the output should be:
LETTERS 10
DIGITS 3

'''

#approach 1

str='hello world! 123'
digit_count=0
letter_count=0
for s in str:
    if s.isdigit():
        digit_count +=1
    elif s.isalpha():
        letter_count +=1

print "LETTERS: ",letter_count
print 'DIGITS: ',digit_count


#approach 2
str='hello world! 123'
dict={'DIGITS':0,'LETTERS':0}
for s in str:
    if s.isdigit():
        dict['DIGITS']+=1
    elif s.isalpha():
        dict['LETTERS']+=1
print "LETTERS: ",dict['DIGITS']
print 'DIGITS: ',dict['LETTERS']

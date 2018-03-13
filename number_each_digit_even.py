'''
Question 12
Level 2

Question:
Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number.
The numbers obtained should be printed in a comma-separated sequence on a single line.

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
'''

valid_numbers=[]
for number in range(1000,3001):
    number = str(number)
    if ((int(number[0])%2==0) & (int(number[1])%2==0) &(int(number[2])%2==0) & (int(number[3])%2==0)):
        valid_numbers.append(number)


print (valid_numbers)



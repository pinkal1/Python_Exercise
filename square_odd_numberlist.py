'''
Question 16
Level 2

Question:
Use a list comprehension to square each odd number in a list. The list is input by a sequence of comma-separated numbers.
Suppose the following input is supplied to the program:
1,2,3,4,5,6,7,8,9
Then, the output should be:
1,3,5,7,9

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.

'''

#Approach 1

numbers=raw_input("Please enter comma seperated numbers:")
numbers=numbers.split(',')
valid_number=[]
for number in numbers:
    if (int(number) %2 != 0):
        valid_number.append(number)
    else:
        pass
print valid_number

#Approach 2

numbers=raw_input("Please enter comma seperated numbers:")
l= [num for num in numbers.split(',') if int(num) %2 !=0]
print ','.join(l)


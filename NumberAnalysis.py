'''
Design a program that asks the user to enter a series of 20 numbers. The program should store the numbers in an array and then display the following data:

•	The lowest number in the array
•	The highest number in the array
•	The total of the numbers in the array
•	The average of the numbers in the array


def Number_analysis(numbers):
    i=[1000000]
    for num in numbers:
        if num<i:
            i=num
    return i
'''

def Number_analysis(numbers):
    numbers = numbers.split(',')
    numbers = sorted(numbers)
    i=100
    for num in numbers:
        if int(num) < i:
            i=num
        print(i)

numbers=input("please enter upto 20 numbers:")
print (numbers)
print (Number_analysis(numbers))
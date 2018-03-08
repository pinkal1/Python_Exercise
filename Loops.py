'''
Read an integer N. For all non-negative integers , print square of num. See the sample for details.

Sample Input 

5
Sample Output 

0
1
4
9
16
'''

def square(num):
    i=0
    for i in range(0,num):
        print (i*i)

num=int(input("Please enter integer num:"))
(square(num))


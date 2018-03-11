#The first  fibonacci numbers are , and their cubes are .

cube = lambda x: x * x * x  # complete the lambda function
def fibonacci(n):
    n1 = 0
    n2 = 1
    count = 0
    l1 = []
    while count < n:
        l1.append(n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count = count + 1
    return l1

# print map(lambda x: x*x*x, reuslt)

n = int(input())
print(list(map(cube, fibonacci(n))))





# Create program to perform Fibonacci series

## Example : Using recursion
def fib1(n):
 if n <= 1:
  return n
 else:
  return fib1(n-1)+fib1(n-2)
 return  n

num = int(input("Please enter number:"))
print('Fibonacci series of',num,'is:')
if num <=0:
 print(num)
else:
 for i in range(num):
    print (fib1(i))




'''
## Example 1: Using looping technique
def fib(n):
 a,b = 1,1
 for i in range(n-1):
  a,b = b,a+b
 return a
print (fib(5))
'''


# Program to find factorial number

def fact(num):
    if num == 0:
        return 1
    else:
        return num * fact(num - 1)


num = input("Please enter number:")
print 'factorial of',num, 'is' ,+fact(num)
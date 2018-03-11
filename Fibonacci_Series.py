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
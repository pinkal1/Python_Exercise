

#USing map function

def calculateSquare(n):
  return n*n

numbers = (1, 2, 3, 4)
result = map(calculateSquare, numbers)
print(result)


#Using lambda
numbers = (1, 2, 3, 4)
result = map(lambda x:x*x,numbers)
print(result)


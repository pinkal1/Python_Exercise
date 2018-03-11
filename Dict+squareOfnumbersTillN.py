#create dictionary with the function which has all integral square numbers.

n=input("Please enter nummber:")

d={}

for i in range(1,n+1):
    d[i] = i*i
print d

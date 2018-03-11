#write a program that takes a list of numbers and makes a new list with only first and last ele
l = [5,10,15,20,25]
print (l[0])
print (l[len(l)-1])

#Using function

def list_end(l):
    return (l[0],l[len(l)-1])


list_end(l)
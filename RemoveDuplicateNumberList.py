#With a given list [12,24,35,24,88,120,155,88,120,155], write a program to print this list after removing all duplicate values with original order reserved.

'''
numberList =[12,24,35,24,88,120,155,88,120,155]

d={}
for number in numberList:
    d[number]=1

print d.keys()
'''


numberList =[12,24,35,24,88,120,155,88,120,155]
uniqueList=[]
for number in numberList:
    if number not in uniqueList:
        uniqueList.append(number)
    else:
        pass

print uniqueList





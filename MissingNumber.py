def missingNumber(list1,list2):
    missinglist = []
    for element in list1:
        if element not in list2:
            missinglist.append(element)
    return missinglist
list1= [1,2,3,4,5,6,7]
list2=[3,7,2,1,4,6]
print missingNumber(list1,list2)
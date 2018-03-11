# Find index of search element.

def find_index(list,searcgEle):
    for element in list:
        if element == searchEle:
            return list.index(element)


list=[1,2,3,4]
searchEle= 3
print find_index(list,searchEle)

'''
#Given sorted array, find location of given string      'ball'   ['at','','','','ball','','','car','','']   output:4

def findIndex(stringList,serachString):
    for word in stringList:
        if word == serachString:
            return stringList.index(word)

stringList = ['at','','','','ball','','','car','','ball']
serachString='baljl'
print findIndex(stringList,serachString)
'''
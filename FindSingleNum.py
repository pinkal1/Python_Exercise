#Given an array of integers, every element appears twice except for one. Find that single one.

def findSingleNum(listofNums):
    d={}
    targetVal=1
    for num in listofNums:
        if num not in d.keys():
            d[num] = 1
        else:
            d[num] += 1
    for key in d:
        if d[key] == targetVal :
            print  key

listofNums=[1,2,3,2,1,4,4,5,7,5,1]
print findSingleNum(listofNums)


# works if numbes comes two times and one time. if same nubmes apears three time then wont work,
'''
def singleNum(listofNums):
    single=[]
    for i in listofNums:
        if i not in single:
            single.append(i)
        else:
            single.remove(i)
    return single



listofNums=[1,2,3,2,1,4,4,5,7,5]
print singleNum(listofNums)
'''
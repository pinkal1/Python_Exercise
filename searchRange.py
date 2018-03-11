
def search(list,SearchNum):
    d={}
    for i in range(0,len(list)):
        d[i]=list[i]

    l=[]
    for k,v in d.items():
        if v == SearchNum:
            l.append(k)
    return  l

list = [1,2,3,4,8,8,2,8]
SearchNum=8
print search(list,SearchNum)
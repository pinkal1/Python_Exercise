#1) using set    Set is collection of element where no element is repeated.

l = ["aaa","bbb","aaa"]
print ("Original list:",l)

l = set(l)
print(l)

#2) Using loop

l = ["aaa","bbb","aaa"]
l1= []
for ele in l:
    if ele not in l1:
        l1.append(ele)
print (l1)
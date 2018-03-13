# Given two lists, return a list of elements that appear in  both.

import random_file

l1 = [1,2,3]
l2 = [2,3,4]
new_list=[]
for ele in l2:
    if ele in l1:
        new_list.append(ele)
print(new_list)

print("-------------------------------------------")

l1 = [1,2,3]
l2 = [2,3,4]
print (list(set(l1).intersection(l2)))

print("-------------------------------------------")

l1 = [1,2,3]
l2 = [2,3,4]
new_list=[]
t =[ele for ele in l2 if ele in l1]
print(t)

print("-------------------------------------------")

l1 = [1,2,3]
l2 = [2,3,4]
for num in l2:
    if num not in l1:
        l1.append(num)
print (l1)

# another way

first_list = random_file.sample(range(10), 5)
print(first_list)
second_list = random_file.sample(range(10), 5)
print(second_list)
for num in second_list:
    if num not in first_list:
        first_list.append(num)
print(first_list)


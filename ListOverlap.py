import random
l1 = [1,2,3]
l2 = [2,3,4]
for num in l2:
    if num not in l1:
        l1.append(num)
print (l1)

# another way

first_list = random.sample(range(10),5)
print(first_list)
second_list = random.sample(range(10),5)
print(second_list)
for num in second_list:
    if num not in first_list:
        first_list.append(num)
print(first_list)
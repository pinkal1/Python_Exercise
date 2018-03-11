#Write a program that prints all elements of list that are less than 5.
l = [1,1,2,3,5,8,13,21,34,55,80,4]
newl = []
for num in l:
    if num < 5:
        newl.append(num)
print(newl)

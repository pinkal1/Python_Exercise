#program to replace char in string. Example: k-m, 0-q e-g
str='kom'
print str
index = 0
newstr = []
while index < len(str):
    if str[index] == 'k':
        l1= str[index].replace(str[index],'m')
        newstr.append(l1)
        index = index+1
    elif str[index] == 'o':
        l1= str[index].replace(str[index],'q')
        newstr.append(l1)
        index = index+1
    else:
        newstr.append(str[index])
        index = index + 1

print newstr



'''
#Using string reverse
origstr = "madam"
revstr = origstr[::-1]
if origstr == revstr:
    print("Palindrome")
else:
    print("Not palindrome")
'''


#using loop

def is_palim(str):
    str1 = ''
    for i in range(len(str)):  # range starts from 0,1,2,3,4,5    len is 6  example str='pinkal'
        str1 += str[len(str) - 1 - i]
    if str1 == str:
        return True
    else:
        return  False



str = [
    "racecar",
    "kayak",
    "never odd or even",
    "rats live on no evil star",
    "A Toyota! Race fast... safe car: a Toyota",
    "Some men interpret nine memos",
    "wombat",
    "No trace; not one cartoon",
    "Ma'am, I'm Adam",
    "Del was a sled",
    "Flee to Em, remote elf",
    "Ma? Ha! A sham!"
]
str= [word.lower() for word in str]
str= [word.spilt(' ') for word in str]
str= (' ').join(str)
for word in str:
    print word,is_palim(word)


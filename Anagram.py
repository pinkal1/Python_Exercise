#Given two strings, write a method to decide if one is a permutation of the other.   Example: public relations   crap built on lies


'''
def anagram(str1,str2):
    return sorted(str1) == sorted(str2)

str1= raw_input("Enter string 1:")
str2= raw_input("Enter string 2:")
str1=str1.replace(' ','')
str2=str2.replace(' ','')
print anagram(str1,str2)

'''


def anagram(str1,str2):
    if len(str1) != len(str2):
        return False

    count ={}

    for char in str1:
        if char in count:
            count[char] += 1
        else:
            count[char]=1

    for char in str2:
        if char in count:
            count[char] -= 1
        else:
            count[char] = 1

    for k in count:
        if count[k] != 0:
            return False
    return True

str1=raw_input("Please enter:")
str1=str1.replace(' ','')
str2=raw_input("Please enter:")
str2=str2.replace(' ','')
print anagram(str1,str2)

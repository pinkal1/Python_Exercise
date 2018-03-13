'''
Write a function that takes a string as input and returns the string reversed.

Example:
Given s = "hello", return "olleh".
'''
def reverseString(s):
    return s[::-1]

s='hello'
print (reverseString(s))


def reverseString(s):
    rev_str=[]
    for char in s[::-1]:
        rev_str.append(char)
    return ''.join(rev_str)




s='hello'
print (reverseString(s))
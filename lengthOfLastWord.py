'''Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space characters only.'''

def lengthOfLastWord(s):
    return 0 if len(s.split()) == 0 else len(s.split()[-1])


s="hi pibk  "
print(lengthOfLastWord(s))

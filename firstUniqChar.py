'''
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.
 

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.

'''

'''
#this exceeds time limit

def firstUniqChar(s):
    index = [s.index(char) for char in s if s.count(char) == 1]
    return min(index) if len(index) > 0 else -1
'''

def firstUniqChar(s):
    return min([s.index(c) for c in s if s.count(c)==1] or [-1])

s='cc'
print (firstUniqChar(s))

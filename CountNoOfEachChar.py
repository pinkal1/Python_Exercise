'''program which count and print the numbers of each character in a string input by console.

Example:abcdefgabc
output
a,2
c,2
b,2
e,1
d,1
g,1
f,1
'''

'''
string='asba'
d={}
for ch in string:
    count = 1
    if ch in d:
        d[ch] = d.get(ch,0)+1
    else:
        d[ch] = count
print d
'''



string = 'absda'
d={}
for char in string:
    if char in d.keys():
        d[char]=d[char]+1
    else:
        d[char]=1
print d
print '\n'.join(['%s,%s' % (k, v) for k, v in d.items()])
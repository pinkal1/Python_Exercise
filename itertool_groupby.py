from itertools import groupby
'''
input : [2,6,8,9,10]
Output: [(2, 2), (6, 6), (8, 10)]
'''

l=[2,6,8,9,10]
def make_range(l):
    for a,b in groupby(enumerate(l),lambda (x,y):y-x):
        b=list(b)
        yield b[0][1],b[-1][1]
print list(make_range(l))
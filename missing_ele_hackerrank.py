
'''
Given an array of integers from 1 to 100 with one or multiple missing integers.
if there is one missing integer, return only tthat number.
if there are multiple consecutive integers, return range.

i/p  {2,3,99}   op 1,[4,98],100

[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
[1, 3, 4, 6, 8, 9, 10, 11, 12, 13, 14]
----------------
[(1, 1), (3, 4), (6, 6), (8, 14)]
[1, (3, 4), 6, (8, 14)]

'''
from itertools import groupby, count
def missing_values(list_of_num):

    list_1_100=list(range(1,101))
    #print(list_1_100)
    missing_list= [x for x in list_1_100 if x not in list_of_num]
    print(missing_list)

    def make_range(missing_list):
        for a, b in groupby(enumerate(missing_list), lambda (x, y): y - x):
            b = list(b)
            yield b[0][1], b[-1][1]
    #l=[1, 3, 4, 6, 8, 9, 10, 11, 12, 13, 14]
    #print list(make_range(l))
    def delete_duplicate_tuple(t):
        min_t,max_t= t
        if min_t == max_t:
         return min_t
        else:
            return (min_t,max_t)
    #t=(1,2)                            # (1,2)  ->(1,2)   (1,1) -> 1
    #print delete_duplicate_tuple(t)

    return map(delete_duplicate_tuple,list(make_range(missing_list)))

list_of_num=[2,3,99]
print missing_values(list_of_num)


#Please write a program which prints all permutations of [1,2,3]

'''
import itertools
print list(itertools.permutations([1,2,3]))
'''

#Write a program to check if sting 1 is permutation of string 2:
'''
ab   ab   True
abv  ba   False
Ab   ba   True
a    aa   False
'''



# multiply s2, Example : abcabc now check if string 1 is in sided this multiplied string
def is_permuation(s1,s2):
    if len(s1) == len(s2):
        s2=s2*2
        if s1 in s2:
            return True
        else:
            return  False
    else:
        return False



# sort both string and chek if they are same
def is_permutation1(s1,s2):
    return sorted(s1)==sorted(s2)




s1=raw_input()
s2=raw_input()
print is_permuation(s1,s2)
print is_permutation1(s1,s2)



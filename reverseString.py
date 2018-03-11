# Write a code to reverse string   "abcd"  -->  "dcba"


'''def reverse(string):
    index = 0
    rev_str=''
    for i in range(0,len(string)):
        rev_str +=string[len(string)-1-i]    # loop from backword
    return rev_str

string = 'hello'
print reverse(string)'''

def reverse(string):
    return string[::-1]

string=raw_input("Please enter string:")
print reverse(string)
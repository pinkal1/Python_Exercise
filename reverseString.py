# Write a code to reverse string   "abcd"  -->  "dcba"


def reverse1(string):
    index = 0
    rev_str=''
    for i in range(0,len(string)):
        rev_str +=string[len(string)-1-i]    # loop from backword
    return rev_str

def reverse2(s):
    i=len(s)-1
    rev_str=''
    while i >=0:
        rev_str+=s[i]
        i=i-1
    return rev_str

def reverse3(string):
    return string[::-1]

def reverse4(string):
    r = ""
    for c in string:
        r= c+r
    return r

string=input("Please enter string:")
print (reverse1(string))
print (reverse2(string))
print (reverse3(string))
print (reverse4(string))


b='hello world'
print(''.join(reversed(b)))

print ("--------------------------------------------------------------------")


# Reverse list

os = ['Windows', "macOS" , "Linux"]
print('Original list:',os)

os.reverse()
print('Reversed List',os)

os = ['Windows', "macOS" , "Linux"]
rev=os[::-1]
print('Reversed List',rev)

os = ['Windows', "macOS" , "Linux"]
for o in reversed(os):
    print(o)

list_data= ['Windows', "macOS" , "Linux"]
rev_lst=[]
l = len(list_data)-1
while l >=0:
    rev_lst.append(l)
print( rev_lst)

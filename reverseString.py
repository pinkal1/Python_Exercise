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

string=input("Please enter string:")
print (reverse(string))

#reverse string

a='hello world'[::-1]
print(a)

b='hello world'
print(''.join(reversed(b)))

def reverse(s):
    r = ""
    for c in s:
        r= c+r
    return r
s="hello world"
print(reverse(s))




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
#print(len(list_data))
l = len(list_data)
i=l+1
rev_data = []
while l>0:
  j=i-l
  l-=1
  rev_data.append(list_data[-j])
print ("After Rev:- %s" %rev_data)

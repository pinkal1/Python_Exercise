# String written as " " or ' '. len(s) to find length. Use [] to access individual char. index start with 0. Use + to join string together.
s='Hello'
print (len(s))   #5
print (s[0])     #h
print(s[4])      #o


s1= " Hi"
print(s+s1)

#Slicing: way of refering subpart. syntatx is s[i:j]    i means start with index.  J means upto but ont including.

str1="jay"
for i in str1:
    print (i)
print (str1[::-1])


# count no of S in string
strnew = 'superman Sing the shower'
count = 0
for c in strnew:
    if ('s' in c ) or ('S' in c):
        count = count + 1
print (count)

#replace vowel with '_'
strnew = 'superman Sing the shower'
strnew1 =''
for c in strnew:
    if  (c in 'a') or (c in 'e') or (c in 'i') or (c in 'o') or (c in 'u') :
        strnew1 += '-'
    else:
        strnew1 += c
print(strnew1)

#write a function which accepts three arguments a string, character to search for and replacement character
def strreplace(str1,str2,str3):
    updatestr = ''
    for c in str1:
        if c == str2:
            updatestr += str3
        else:
            updatestr+=c
    return  updatestr

print(strreplace('hi how are','h','i'))

# function which accepts two arguments, string and single character. return no of time that char found.
def CharOccur(str1,char):
    count = 0
    for c in str1:
        if char in c:
            count += 1
    return count

print(CharOccur("hi how are you hi ho",'h'))


import string
# given string capital each word       .upper()  for capitalization
#str = input()
#print (str.upper())


#print (string.capwords(str))
str = 'hi hi how are'
str1= ' '.join(c[0].upper() + c[1:] for c in str.split())
print (str1)
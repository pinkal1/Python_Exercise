#Write a program which accepts a sequence of words separated by whitespace as input to print the words composed of digits only. 2 cats and 3 dogs. ['2', '3']


import re
str=raw_input("Please enter:")
print re.findall('\d+',str)
#Python Program to Detect if Two Strings are Anagrams

str1= raw_input("Enter string 1:")
str2= raw_input("Enter string 2:")


if sorted(str1) == sorted(str2):
    print ("yes")

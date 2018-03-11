#Python program to find number of vowel in string
vowel='aeiou'
ip_string='howareyou'
count=0
for i in ip_string:
    for j in vowel:
        if i == j:
            count = count+1
print count
# Print the first repeating character   asked during QA interview
# Example: input: 123LK63824K output: 3


string='123LK63824K'
d={}
for char in string:
    if char in d.keys():
        print char
        break
    else:
        d[char] =0

print "----------------------------------------"

# example: word="aaaabbcccaahhhhhhah"   op h: 6   not h:7   hould be consecutive char

word = "aaaabbcccaahhhhhhah"
count = 1
length = dict()
for i in range(1, len(word)):
    if word[i - 1] == word[i]:
        count += 1
    else:
        length[str(count)] = word[i - 1]
        count = 1
length[str(count)] = word[i]
print (length)

print max(length.keys()), length[max(length.keys())]




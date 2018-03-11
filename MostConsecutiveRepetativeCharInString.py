# example: word="aaaabbcccaahhhhhhah"   op h: 6   not h:7   hould be consecutive char


word="aaaabbcccaahhhhhhah"

print len(word)


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

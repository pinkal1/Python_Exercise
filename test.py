
word ='aaba'
count = 1
d = {}
for i in range(1, len(word)):
    if word[i - 1] == word[i]:
        count = count + 1
    else:
        d[str(count)] = word[i - 1]
        count=1
d[str(count)] = word[i]
print(d)
print (max(d.keys()), d[max(d.keys())])




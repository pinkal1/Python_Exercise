words="olly olly in come free"
words=words.split(' ')
dict={}
for word in words:
    print (word)
    if word not in dict:
        dict[word] =1
    else:
        dict[word] = dict[word] + 1
dict =[(k,v) for k,v in dict.items()]
print(dict)


def findSubstring(s,words):
    concate_words = []
    concate_words.append(''.join(map(str,words[::-1])))
    concate_words.append(''.join(map(str,words)))
    print (concate_words)
    index_of_Word=[]
    for word in concate_words:
        if word in s:
            index_of_Word.append(s.index(word))
    return index_of_Word


s= "barfoothefoobarman"
words= ['foo','bar']
print (findSubstring(s,words))


def FindLongestWord(sententence):
    d={}
    for word in sententence.split(' '):
        d[word] = (len(word))
    key_max = max(d.keys(), key=(lambda k: d[k]))
    print('Longest word: ',(key_max),' with length of:', d[key_max])
    return d

sententence = 'This 7 67868798 is a United State.'
print(FindLongestWord(sententence))


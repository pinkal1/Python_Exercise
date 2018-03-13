def append_s(words):
    new_words = []
    for word in words:
        new_words.append(word + 's')
    return new_words

words=['a', 'b', 'c']
print(append_s(words))


def append_s(words):
    return [word+'s' for word in words]

words = ['a', 'b', 'c']
print(append_s(words))



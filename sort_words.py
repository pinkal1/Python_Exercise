'''
Question:
Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.
Suppose the following input is supplied to the program:
without,hello,bag,world
Then, the output should be:
bag,hello,without,world

'''
def sorting_words(words):
    words=words.split(',')
    words=sorted(words)
    return ','.join(words)


words=input("Please enter comma seperated words:")
print (words)
print(sorting_words(words))

'''
Question 10
Level 2

Question:
Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words and sorting them alphanumerically.
Suppose the following input is supplied to the program:
hello world and practice makes perfect and hello world again
Then, the output should be:
again and hello makes perfect practice world

'''
#approach 1

def sorting_words_alpha(words):
    words=words.split(' ')
    words=sorted(words)
    no_duplicate=[]
    for word in words:
        if word not in no_duplicate:
            no_duplicate.append(word)
        else:
            pass

    return ' '.join(no_duplicate)
words=input("Please enter whitespace seperated input of words:")
print(sorting_words_alpha(words))


#approach 2
words=input("Please enter whitespace seperated input of words:")
word=[word for word in words.split( )]
print (' '.join((sorted(list(set(word))))))

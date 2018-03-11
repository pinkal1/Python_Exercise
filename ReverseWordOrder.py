# Write a program that ask the user for long string containing multiple words and print them back order

str = "Hi How are you"
result = []
#print (str.split(' '))       #['Hi', 'How', 'are', 'you']
word = (str.split(' '))
#print (word[1])       #How
for ele in range(len(word)):
    result.append( (word[(len(word) - 1- ele) ]))
#print (result)              # ['you', 'are', 'How', 'Hi']

print (' '.join(result))      # you are How Hi


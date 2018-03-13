'''
How do you get a random line from a large file
'''

import random

filesize = 1500                 #size of the really big file
offset = random.randrange(filesize)


f = open(r'C:\Users\Jay\Desktop\Python\large.txt','r+')
f.seek(offset)                  #go to random position
f.readline()                    # discard - bound to be partial line
random_line = f.readline()      # bingo!

# extra to handle last/first line edge cases
if len(random_line) == 0:       # we have hit the end
    f.seek(0)
    random_line = f.readline()  # so we'll grab the first line instead
print(random_line)


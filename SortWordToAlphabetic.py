# sort string of words into alphabetical order

ip_string = 'hi how are you'
print ("Entered string:")+ip_string
listofWords =  ip_string.split(' ')
sortedList=sorted(listofWords)
print (' '.join(sortedList))
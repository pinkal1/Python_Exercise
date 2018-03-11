# Print all numbers divisible by 7 and not multiple of 5 between (2000 and 3201).   Note all number must be comma seperated list.



answerlist=[]
for num in range(2000,3201):
    if ((num%7 == 0) and (num % 5 !=0)):
        answerlist.append(str(num))


print (','.join(answerlist))
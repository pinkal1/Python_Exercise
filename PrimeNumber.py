#Write a program to find Prime number

no=9

for i in range(2,no):
    if no % i != 0 and no % 1 == 0:
        print ('prime')
        break
    else:
       print ('not Prime')
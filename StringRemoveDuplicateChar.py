#remove duplicate characters in a string

#string='SSYYNNOOPPSSIISS'
#ans= 'SYNOPI'
'''
def removeDuplicate(string):
    uniquqChar = ''
    for i in string:
        if i not in uniquqChar:
            uniquqChar += i
    return  uniquqChar

string='SSYYNNOOPPSSIISS'
print removeDuplicate(string)'''


#string='SSYYNNOOPPSSIISS'
#ans= 'SYNOPI'


def RemoveDupliChar(Word):
    uniquqChar = ' '
    index=0
    for char in Word:
        if char != uniquqChar[index]:
            uniquqChar += char
            index += 1
    return uniquqChar

print (RemoveDupliChar('SSYYNNOOPPSSIISS'))

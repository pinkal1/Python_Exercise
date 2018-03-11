def replaceCharInString(string,char,pos):
    l = list(string)
    l[pos]=char
    return ''.join(l)

string = input("Please enter string:")
char = input("Please enter replacement character:")
pos = input("Please enter position:")
print (replaceCharInString(string,char,int(pos)))
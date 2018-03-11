#replace all spaces in a string with '%20'



def replace(str):
    newstr=''
    for i in str:
        if i == ' ':
            newstr += '20'
        else:
            newstr += i
    return newstr


print replace('pink lljh jhjj')

#waterbottle is rotation of erbottlewat   hello  llohe  lloh  ohlle  ohell

def is_rotation(str1, str2):
    return(len(str1) == len(str2) and str1 in str2*2)


str1='hello'
str2='ohell'
print is_rotation(str1, str2)

'''
def is_rotation(str1, str2):
    if len(str1) != len(str2):
        return False

    for index in xrange(len(str1)):
        if str2.startswith(str1[index:]) and str2.endswith(str1[:index]):
            return True

    return False
'''
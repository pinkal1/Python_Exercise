# Determine whether or not a given string contains no duplicate characters.

def is_unique(string1):
    uniqieList=[]
    for char in string1:
        if char in uniqieList:
            return False
        else:
            uniqieList.append(char)
    return  True

string1= raw_input("Please enter string :")
print is_unique(string1)
'''
Input:  str1 = "aab", str2 = "xxy"
Output: True
'a' is mapped to 'x' and 'b' is mapped to 'y'.
'''


def isIsomorphic(string1, string2):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    if not string1 and not string2:
        return True
    elif string1 and string2:
        if len(string1) != len(string2):
            return False
        elif len(set(string1)) != len(set(string2)):
            return False
        else:
            mapping = {}
            for i in range(len(string1)):
                if string1[i] in mapping:
                    if mapping[string1[i]] != string2[i]:
                        return False
                else:
                    mapping[string1[i]] = string2[i]
        return True
    else:
        return False


print (isIsomorphic('axa', 'cyc'))
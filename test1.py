'''Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.'''


def isValid( s):
        stack = []
        dict = {"]":"[", "}":"{", ")":"("}
        if len(s) >=2:
            for char in s:
                if char in dict.values():
                    stack.append(char)
                elif char in dict.keys():
                    if stack == [] or dict[char] != stack.pop():
                        return False
                else:
                    return False
            return True
        else:
            return False
#print(isValid('()'))
#print(isValid('()[]{}'))
#print(isValid('(]'))
print(isValid('['))
#print(isValid('[}'))

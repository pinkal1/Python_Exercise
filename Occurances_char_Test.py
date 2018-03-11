import re

#[('a',5),('b',3),('c',1)]   True    [('x',2),('b',3),('c',5)]  False
def is_char_in_alphabeticalorder(output):
    prev_count= None
    prev_char=None
    for char,count in output:
        if prev_count == None:
            prev_count = count
        elif prev_count < count:
            return False
        elif prev_count == count:
            if prev_char == None:
                prev_char = char
            elif ord(prev_char) <ord(prev_char):
                return False
        prev_char = char
        prev_count = count
    return True

def non_alpha_whiteSpace(output):
    for char,count in output:
        if len(char) > 1:
            return False
        if re.match('^[a-zA-Z]',char) is None:
            return False
    return  True

def distinct_case_ignored(output):
    list_of_char = map(lambda (c,i):c,output)
    all_upper= map(lambda c: c.upper(),list_of_char)
    all_upper = set(all_upper)
    return  len(all_upper) == len(list_of_char)

output = [('u', 5), ('b', 4), ('U', 1)]
print (is_char_in_alphabeticalorder(output))
print (non_alpha_whiteSpace(output))
print (distinct_case_ignored(output))
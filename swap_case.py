def swap_case(s):
    s_new=''
    for char in s:
        if char.lower():
                s_new.append(char.upper())
        else:
            s_new.append(char.lower())
    return s_new

s='Pinkal'
print(swap_case(s))
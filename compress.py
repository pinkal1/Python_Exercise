
import functools

def compress(chars):
    dict = {}
    for char in chars:
        if char not in dict:
            dict[char] = 1
        else:
            dict[char] = dict[char] +1

    return  list(functools.reduce(lambda x, y: x + y, dict.items()))

chars=["a","b","b","b","b","b","b","b","b","b","b","b","b"]
print (compress(chars))





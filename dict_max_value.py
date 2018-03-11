#Write a Python program to get the maximum value with respected key in a dictionary.
'''d={'x':3,'y':7,'z':2}
print (d)
ll=[d[i] for i in d]
print (ll)
key_of_max_value=(max(d.keys(), key=(lambda k:d[k])))
print (key_of_max_value)
print (d[key_of_max_value])

max([d[i] for i in d])
'''


d={'x':3,'y':7,'z':2}

# get valuees from dict
value_dict=[d[i] for i in d]
print(value_dict)                        # [3, 7, 2]

key_of_max_value = max(d.keys(), key=(lambda i: d[i]))

print (d[key_of_max_value])              #  7
print (key_of_max_value)                 #  y
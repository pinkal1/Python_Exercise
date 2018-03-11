# Print the first repeating character   asked during QA interview
# Example: input: 123LK63824K output: 3


def first_repeating_char(string):
    d={}
    for char in string:
        if char in d.keys():
            print ("First repeating character is :",char)
            break
        else:
            d[char] =0

string='123LK63824K'
print ("string is: ",string)
first_repeating_char(string)

print ("----------------------------------------")

# example: word="aaaabbcccaahhhhhhah"   op h: 6   not h:7   should be consecutive char

def most_consecutive_char(string):
    count = 1
    d = {}
    for i in range(1, len(string)):
        if string[i - 1] == string[i]:
            count += 1
        else:
            d[str(count)] = string[i - 1]
            count = 1
    d[str(count)] = string[i]
    print (d)
    print (max(d.keys()), d[max(d.keys())])
    print(d[max(d.keys())],'occurs', max(d.keys()),'times')

string = "aaaabbcccaahhhhhhah"
print ("string is: ",string)
most_consecutive_char(string)





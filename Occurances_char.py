import re

#string='pinkala'
def count_occurances(s):
    non_alpha_s = re.compile('[^\w]').sub('',s).upper()

    d={}
    for ch in non_alpha_s:
        if ch in d.keys():
            d[ch]=d[ch]+1
        else:
            d[ch] = 1

    output = d.items()
    output = sorted(output,key=lambda (char,count):(-count,char))
    return  output

def  count_occurances_visual(s):
    output = count_occurances(s)
    for (char,count) in output:
        print ('{char}:{count}'.format(char=char,count = count))

#s= raw_input()
s='Twi%tt**er is awes/om& e%'
print  (count_occurances_visual(s))
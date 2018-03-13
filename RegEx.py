

import re

def numbers(s):
    m=re.search(r'\d+',s)
    return m.group()

s='hkjjh3k12'
print (numbers(s))

s = "Your number is <b>123</b>"

m = re.search(r"\d+", s)
print (m.group())


nameage = '''
Pinkal is 21 and Xys is 300
Abc is 49

'''
age = re.findall(r'\d{1,3}',nameage)
print (age)

name= re.findall(r'[A-Z][a-z]*',nameage)
print (name)

phn= '''
123-345-6787
12-345-6789
acs-sdd-ssds
111-222-3333
'''
valid = re.findall(r'\d{3}-\d{3}-\d{4}',phn)
print (valid)

fullname= '''
jiya varma
Hinapatil
Riya 
Ciya Patel

'''
validfullname = re.findall(r'\w{1,20}\S\w{1,20}',fullname)
print(validfullname)


email='''
xyz@gmail.com  sa dsa da
g.com d
pqre1@. 121
y@q.com  eq13 214
p.p@gmail.com
'''
valid_email=re.findall(r'[a-zA-Z._+-]{1,20}@\w{1,20}.[com|edu|org]{3}',email)    # if '-' is at the end no need to escap it '\-'
print(valid_email)

ip_address='''
xxx.xxx.xxxx
111.111.1111
fsd.fsd.fsd
23.32123.23

'''
ip_pattern='(\d{3}.\d{3}.\d{4})'
valid_ip=re.findall(ip_pattern,ip_address)
print (valid_ip)
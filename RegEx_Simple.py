import re

#match phonenumber
fh = open('C:\Users\Jay\Desktop\PythonCoding\simple.txt')
pattern = re.compile(r'\d\d\d[.-]\d\d\d[.-]\d\d\d\d')
for line in fh:
    for match in pattern.findall(line):
        print match
fh.close()


'''
# find phone number     [.-] matches . or -
pattern = re.compile(r'\d\d\d[.-]\d\d\d[.-]\d\d\d\d')

321-555-4321
123.555.1234
800-555-1234
900-555-1234

'''
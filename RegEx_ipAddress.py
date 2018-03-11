import re

#match ipAddress   xxx.xxx.xxxx
fh = open('C:\Users\Jay\Desktop\PythonCoding\ipAddress.txt')
pattern = re.compile(r'\d{3}[.]\d{3}[.]\d{4}')
for line in fh:
    for match in pattern.findall(line):
        print match
fh.close()


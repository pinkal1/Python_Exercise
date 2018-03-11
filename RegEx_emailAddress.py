import re

fileText='''should we use regex more often? let me know at  321dsasdsa@dasdsa.com.lol" \
      
Corey.MSchafer@gmail.com
corey.schafer@university.edu
corey-321-schafer@my-work.net
   '''
pattern=(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+')
match = re.findall(pattern,fileText)
print match


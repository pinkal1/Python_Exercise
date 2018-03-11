import re

urls = '''
https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov
'''
pattern=(r'https?://\w+.\w+.\w{3}')
match = re.findall(pattern,urls)
print match


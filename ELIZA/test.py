import re 

# re.findall(the )

p = re.compile(r'the (.*)er they (.*), the \1er we \2')

print(p.search('the faster they ran, the faster we ran').group())

# print(p.search('the faster they ran, the faster we ate').group())
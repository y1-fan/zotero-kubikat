import sys, codecs, re

str = input("Input file name:")

f = open(str,"r",encoding = 'windows-1252')
text = f.read()
f.close()

text = text.replace('<<','')
text = text.replace('>>','')
text = re.sub('TI  - (.+)\nTI  - (.+)','TI  - \g<1>\n: \g<2>',text)

f = open(str,"w",encoding = 'UTF-8')
f.write(text)
f.close()
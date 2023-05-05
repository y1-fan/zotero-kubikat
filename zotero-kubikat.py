import sys, codecs, re

str = input("Input file name:")

f = open(str,"r",encoding = 'windows-1252')
text = f.read()
f.close()

text = text.replace('<<','')
text = text.replace('>>','')

f = open(str,"w",encoding = 'UTF-8')
f.write(text)
f.close()
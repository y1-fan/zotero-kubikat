import sys, codecs, re

str = input("Input file name:")

f = open(str,"r",encoding = 'windows-1252')
text = f.read()
f.close()

text = text.replace('<<','')
text = text.replace('>>','')
text = re.sub('TI  - (.+)\nTI  - (.+)','T1  - \g<1>\n: \g<2>',text)
text = text.replace('QS','CN')
text = re.sub('TT  - (.+)\nTT  - (.+)','N1  - Translated Title: \g<1>\n: \g<2>',text)
text = re.sub('AV  - (.+)\nAV  - (.+)','AV  - \g<1>\n; \g<2>',text)
text = re.sub('AV  - (.+)\nAV  - (.+)\nAV  - (.+)','AV  - \g<1>\n; \g<2>\n; \g<3>',text)
text = re.sub('AV  - (.+)\nAV  - (.+)\nAV  - (.+)\nAV  - (.+)','AV  - \g<1>\n; \g<2>\n; \g<3>\n; \g<4>',text)

f = open(str,"w",encoding = 'UTF-8')
f.write(text)
f.close()
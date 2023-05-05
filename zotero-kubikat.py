import sys, codecs, re

str = input("Input the RIS file path:")

f = open(str,"r",encoding = 'windows-1252')
text = f.read()
f.close()

text = text.replace('<<','')
text = text.replace('>>','')
text = re.sub('TI  - (.+)\nTI  - (.+)','TI  - \g<1>\n: \g<2>',text)
text = text.replace('QS','CN')
text = re.sub('TT  - (.+)\nTT  - (.+)','N1  - Translated Title: \g<1> : \g<2>',text)
text = re.sub('AV  - (.+)\nAV  - (.+)','AV  - \g<1>\n; \g<2>',text)
text = re.sub('AV  - (.+)\nAV  - (.+)\nAV  - (.+)','AV  - \g<1>\n; \g<2>\n; \g<3>',text)
text = re.sub('AV  - (.+)\nAV  - (.+)\nAV  - (.+)\nAV  - (.+)','AV  - \g<1>\n; \g<2>\n; \g<3>\n; \g<4>',text)
text = re.sub('TY  - JOUR\n((.+\n)+)CY  - (.+)','TY  - CHAP\n\g<1>CY  - \g<3>',text)

f = open(str,"w",encoding = 'UTF-8')
f.write(text)
f.close()
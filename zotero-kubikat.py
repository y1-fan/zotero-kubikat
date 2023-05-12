import sys, codecs, re

str = input("Input the RIS file path:")

f = open(str,"r",encoding = 'windows-1252')
text = f.read()
f.close()

text = text.replace('<<','')
text = text.replace('>>','')
text = re.sub('TI  - (.+)\nTI  - (.+)','TI  - \g<1>\n: \g<2>',text)
text = re.sub('TT  - (.+)\nTT  - (.+)','N1  - Translated Title: \g<1> : \g<2>',text)

text = re.sub('AV  - (.+)\nAV  - (.+)\nAV  - (.+)\nAV  - (.+)','AV  - \g<1>\n; \g<2>\n; \g<3>\n; \g<4>',text)
text = re.sub('AV  - (.+)\nAV  - (.+)\nAV  - (.+)','AV  - \g<1>\n; \g<2>\n; \g<3>',text)
text = re.sub('AV  - (.+)\nAV  - (.+)','AV  - \g<1>\n; \g<2>',text)

text = re.sub('TY  - JOUR\n((.+\n)+)CN  - (.+)\((.+)','TY  - CHAP\n\g<1>CN  - \g<3>(\g<4>',text)

text = re.sub('PB  - (.+)\nPB  - (.+)\nPB  - (.+)\nPB  - (.+)','PB  - \g<1>\n; \g<2>\n; \g<3>\n; \g<4>',text)
text = re.sub('PB  - (.+)\nPB  - (.+)\nPB  - (.+)','PB  - \g<1>\n; \g<2>\n; \g<3>',text)
text = re.sub('PB  - (.+)\nPB  - (.+)','PB  - \g<1>\n; \g<2>',text)

text = text.replace('UR','L2')

text = re.sub('SP  - (.+)\nQS  - (.+)','QS  - \g<2>',text)
text = re.sub('SP  - (.+)\n((.+)\n+)QS  - (.+)','\g<1>QS  - \g<4>',text)
text = text.replace('QS','SP')

f = open(str,"w",encoding = 'UTF-8')
f.write(text)
f.close()
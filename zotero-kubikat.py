import sys, codecs, re

str = input("Input the RIS file path:")

#处理编码问题
f = open(str,"r",encoding = 'windows-1252')
text = f.read()
f.close()

#处理多余的‘<<’和‘>>’
text = text.replace('<<','')
text = text.replace('>>','')

#多行标题转写为一行
text = re.sub('TI  - (.+)\nTI  - (.+)','TI  - \g<1>\n: \g<2>',text)

#把译名作为笔记插入
text = re.sub('TT  - (.+)\nTT  - (.+)','N1  - Translated Title: \g<1> : \g<2>',text)

#让多个 AV 同时显示
tmp = re.sub('AV  - (.+)\nAV  - (.+)\n','AV  - \g<1> ; \g<2>\n',text)
while tmp != text:
    text = tmp
    tmp = re.sub('AV  - (.+)\nAV  - (.+)\n','AV  - \g<1> ; \g<2>\n',text)

#对 JOUR 和 CHAP 类型进行区分
text = text.replace('JOUR','CHAP')
text = re.sub('TY  - CHAP\n((.+\n)+)QS  - (.+)\((.+)','TY  - JOUR\n\g<1>QS  - \g<3>(\g<4>',text)

#让多个 PB 同时显示
tmp = re.sub('PB  - (.+)\nPB  - (.+)\n','PB  - \g<1> ; \g<2>\n',text)
while tmp != text:
    text = tmp
    tmp = re.sub('PB  - (.+)\nPB  - (.+)\n','PB  - \g<1> ; \g<2>\n',text)

#把 URL 作为链接存在
text = text.replace('UR  -','L2  -')

#把 SP 条目内容替换为 QS 条目内容
text = re.sub('SP  - (.+)\nQS  - (.+)','QS  - \g<2>',text)
text = re.sub('SP  - (.+)\n((.+)\n+)QS  - (.+)','\g<1>QS  - \g<4>',text)
text = text.replace('QS','SP')

f = open(str,"w",encoding = 'UTF-8')
f.write(text)
f.close()
# 从键盘输入一个字符串，将小写字母全部转换成大写字母，然后输出到一个磁盘文件"test"中保存
f1=open('G:/pythonfile/t6.txt','w+')
mystr=input('请输入一串字符串：')
mystr=mystr.upper()
f1.write(mystr)
f1.close()
f1=open('G:/pythonfile/t6.txt','r')
s=f1.read()
print(s)
f1.close()
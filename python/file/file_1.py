f=open('G:/tan.txt','w+')
f.write('不做无法实现的梦')
f.close()
f=open('G:/tan.txt','r')
mystr=f.read()
print(mystr)
f.close()
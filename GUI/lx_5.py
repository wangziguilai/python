from tkinter import *
root=Tk()
root.title('登录框')
# Canvas(root,width=500,height=700,bg='blue',bd=0)
Label(root,text='账户').grid(row=0,sticky=W)
Label(root,text='密码').grid(row=1,sticky=W)
v=StringVar()
v.set('李丽是傻逼')
e1 = Entry(root,textvariable = v)
e2 = Entry(root)
e1.grid(row = 0,column = 1,sticky = E)
e2.grid(row = 1,column = 1,sticky = E)
Label(root,text = '登录').grid(row = 3,sticky = W+E)
root.mainloop()
import tkinter as tk #import library 

app=tk.Tk()
app.title('Basic Calculator')#title 
app.geometry('300x400')#geometry

val=tk.Variable(app)#define variable as val
tk.Entry(app, textvariable=val,font=10).place(x=35,y=60,width=190,height=30)
global expression
expression=''
#define expression function
def abc(x):
    global expression
    expression=expression+x
    val.set(expression)
#define resultant function
def result(y):
    global expression
    c=str(eval(expression))
    val.set(c)
    expression=''
#define clear function
def clr(z):
    global expression
    expression=''
    val.set(expression)
    
#Numbers button
tk.Button(app, text='1',width=3,command=lambda:abc('1')).place(x=45,y=140)
tk.Button(app, text='2',width=3,command=lambda:abc('2')).place(x=110,y=140)
tk.Button(app, text='3',width=3,command=lambda:abc('3')).place(x=175,y=140)
tk.Button(app, text='4',width=3,command=lambda:abc('4')).place(x=45,y=190)
tk.Button(app, text='5',width=3,command=lambda:abc('5')).place(x=110,y=190)
tk.Button(app, text='6',width=3,command=lambda:abc('6')).place(x=175,y=190)
tk.Button(app, text='7',width=3,command=lambda:abc('7')).place(x=45,y=240)
tk.Button(app, text='8',width=3,command=lambda:abc('8')).place(x=110,y=240)
tk.Button(app, text='9',width=3,command=lambda:abc('9')).place(x=175,y=240)
tk.Button(app, text='0',width=3,command=lambda:abc('0')).place(x=110,y=290)

#Expression button
tk.Button(app, text='.',width=3,command=lambda:abc('.')).place(x=45,y=290)
tk.Button(app, text='/',width=3,command=lambda:abc('/')).place(x=175,y=290)
tk.Button(app, text='=',width=3,command=lambda:result('=')).place(x=235,y=290)
tk.Button(app, text='*',width=3,command=lambda:abc('*')).place(x=235,y=240)
tk.Button(app, text='-',width=3,command=lambda:abc('-')).place(x=235,y=190)
tk.Button(app, text='+',width=3,command=lambda:abc('+')).place(x=235,y=140)
tk.Button(app, text='Clear',width=3,command=lambda:clr('')).place(x=230,y=60,width=50,height=30)
app.mainloop()




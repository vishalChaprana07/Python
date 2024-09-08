from tkinter import *
root=Tk()

value= Entry(root,width=40,borderwidth=5,)
value.grid(row=0,column=0,columnspan=4,padx=10,pady=10)
def add_btn(number):
    value.insert(len(value.get()),number)

def del_last():
    value.delete(0,END)

def addition():
    global last
    last="+"
    global num1 
    num1 = value.get()
    value.delete(0,END)

def calulate():
    global num2
    num2= value.get()

    if(last=="+"):
        res= int(num1) + int(num2)
    if(last=="-"):
        res= int(num1) - int(num2)
    if(last=="*"):
        res= int(num1) * int(num2)

    if(last=="/"):
        if(num1==0):
            value.delete(0,END)
            value.insert(0,"Cannot divide by zero")
            pass
        res= int(num1) / int(num2)

    value.delete(0,END)
    value.insert(0,res)

def subtract():
    global last
    last="-"
    global num1 
    num1 = value.get()
    value.delete(0,END)

def multiply():
    global last
    last="*"
    global num1 
    num1 = value.get()
    value.delete(0,END)

def divide():
    global last
    last="/"
    global num1 
    num1 = value.get()
    value.delete(0,END)
    
    



button1= Button(root,text="1",padx=40,pady=20,command=lambda:  add_btn(1))
button2= Button(root,text="2",padx=40,pady=20,command=lambda:  add_btn(2))
button3= Button(root,text="3",padx=40,pady=20,command=lambda:  add_btn(3))
button4= Button(root,text="4",padx=40,pady=20,command=lambda:  add_btn(4))
button5= Button(root,text="5",padx=40,pady=20,command=lambda:  add_btn(5))
button6= Button(root,text="6",padx=40,pady=20,command=lambda:  add_btn(6))
button7= Button(root,text="7",padx=40,pady=20,command=lambda:  add_btn(7))
button8= Button(root,text="8",padx=40,pady=20,command=lambda:  add_btn(8))
button9= Button(root,text="9",padx=40,pady=20,command=lambda:  add_btn(9))
button0= Button(root,text="0",padx=40,pady=20,command=lambda:  add_btn(0))
button_equal= Button(root,text="=",padx=40,pady=20,command=lambda :calulate())

button_add= Button(root,text="+",padx=40,pady=20,command=lambda :addition())
button_sub= Button(root,text="-",padx=40,pady=20,command=lambda :subtract())
button_mul= Button(root,text="*",padx=40,pady=20,command=lambda :multiply())
button_div= Button(root,text="/",padx=40,pady=20,command=lambda :divide())

button_clr = Button(root,text="clr",padx=40,pady=20,command=del_last)


button1.grid(row=1,column=0,)
button2.grid(row=1,column=1,)
button3.grid(row=1,column=2)
button_add.grid(row=1,column=3)

button4.grid(row=2,column=0 )
button5.grid(row=2,column=1 )
button6.grid(row=2 ,column=2 )
button_sub.grid(row=2,column=3)

button7.grid(row=3 ,column=0)
button8.grid(row=3 ,column= 1)
button9.grid(row=3 ,column= 2)
button_mul.grid(row=3,column=3)

button0.grid(row=4 ,column=0 )
button_equal.grid(row=4,column=1)
button_div.grid(row=4,column=3)

button_clr.grid(row=4,column=2)

root.mainloop()

from tkinter import *
root=Tk()
root.title("Simple Calculator")
#Icon of calculator
root.iconbitmap("calci_FO1_icon.ico")
box=Entry(root,width=35,borderwidth=15)
box.grid(row=0,column=0,columnspan=3,padx=10,pady=10)

def clear(): 
#delete whatever is in the box
    box.delete(0,END)
def click(number):
#insert in the box
    current=box.get()
    box.delete(0,END)
    box.insert(0,str(current)+str(number))   
def add():
    first_num=box.get()
    #take global variable as it can be accesed anywhere
    global f_num
    global math
    math="addition"
    f_num=int(first_num)
    #to delete anything after hitting + symbol
    box.delete(0,END)
def substract():
    first_num=box.get()
    global f_num
    global math
    math="substraction"
    f_num=int(first_num)
    box.delete(0,END)

def multiply():
    first_num=box.get()
    global f_num
    global math
    math="multiplication"
    f_num=int(first_num)
    box.delete(0,END)

def divide():
    first_num=box.get()
    global f_num
    global math
    math="division"
    f_num=int(first_num)
    box.delete(0,END)

def equal():
    #grab the variable
    second_num=box.get()
    box.delete(0,END)
    
    if math=="addition":
        box.insert(0,f_num+int(second_num))

    if math=="substraction":
        box.insert(0,f_num-int(second_num))

    if math=="multiplication":
        box.insert(0,f_num*int(second_num))

    if math=="division":
        box.insert(0,f_num/int(second_num))

#define the buttons
button_1=Button(root,text="1",padx=40,pady=20,command=lambda:click(1),fg="white",bg="black",)
button_2=Button(root,text="2",padx=40,pady=20,command=lambda:click(2),fg="white",bg="black")
button_3=Button(root,text="3",padx=40,pady=20,command=lambda:click(3),fg="white",bg="black")
button_4=Button(root,text="4",padx=40,pady=20,command=lambda:click(4),fg="white",bg="black")
button_5=Button(root,text="5",padx=40,pady=20,command=lambda:click(5),fg="white",bg="black")
button_6=Button(root,text="6",padx=40,pady=20,command=lambda:click(6),fg="white",bg="black")
button_7=Button(root,text="7",padx=40,pady=20,command=lambda:click(7),fg="white",bg="black")
button_8=Button(root,text="8",padx=40,pady=20,command=lambda:click(8),fg="white",bg="black")
button_9=Button(root,text="9",padx=40,pady=20,command=lambda:click(9),fg="white",bg="black")
button_0=Button(root,text="0",padx=40,pady=20,command=lambda:click(0),fg="white",bg="black")
button_add=Button(root,text="+",padx=39,pady=20,command=add,fg="white",bg="black")
button_equal=Button(root,text="=",padx=91,pady=20,command=equal,fg="white",bg="black",borderwidth=5)
button_clear=Button(root,text="Clear",padx=80,pady=20,command=clear,fg="white",bg="black")
button_substract=Button(root,text="-",padx=41,pady=20,command=substract,fg="white",bg="black")
button_multiply=Button(root,text="*",padx=40,pady=20,command=multiply,fg="white",bg="black")
button_divide=Button(root,text="/",padx=40,pady=20,command=divide,fg="white",bg="black")

#put the buttons on screen
button_9.grid(row=3,column=0)
button_8.grid(row=3,column=1)
button_7.grid(row=3,column=2)

button_6.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_4.grid(row=2,column=2)

button_3.grid(row=1,column=0)
button_2.grid(row=1,column=1)
button_1.grid(row=1,column=2)

button_0.grid(row=4,column=0)
button_clear.grid(row=4,column=1,columnspan=2)

button_add.grid(row=5,column=0)
button_equal.grid(row=5,column=1,columnspan=2)

button_substract.grid(row=6,column=0)
button_multiply.grid(row=6,column=1)
button_divide.grid(row=6,column=2)

root.mainloop()
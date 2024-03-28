from tkinter import *
from PIL import Image,ImageTk
from random import *

root=Tk()
root.title("Rock paper Scissor")
root.configure(background="black")
root.minsize(1400,550)
root.maxsize(1400,600)
root.iconbitmap("spricon.ico")

#Images
rock_img=ImageTk.PhotoImage(Image.open("rock_image.png"))
paper_img=ImageTk.PhotoImage(Image.open("paper2.png"))
scissor_img=ImageTk.PhotoImage(Image.open("scissors_image.png"))

#Inserting Images
user_label=Label(root,image=rock_img,bg="black")
comp_label=Label(root,image=scissor_img,bg="black")
user_label.grid(row=1,column=0)
comp_label.grid(row=1,column=4)

#Scores
player_score=Label(root,text=0,font=100,bg="black",fg="white")
comp_score=Label(root,text=0,font=100,bg="black",fg="white")
player_score.grid(row=1,column=1)
comp_score.grid(row=1,column=3)

#buttons
rock=Button(root,width=20,height=2,text="ROCK",bg="white",fg="black",borderwidth=3,command=lambda:updateimages("ROCK"))
paper=Button(root,width=20,height=2,text="PAPER",bg="pink",fg="black",borderwidth=3,command=lambda:updateimages("PAPER"))
scisscor=Button(root,width=20,height=2,text="SCISSOR",bg="yellow",fg="black",borderwidth=3,command=lambda:updateimages("SCISSOR"))
rock.grid(row=2,column=1)
paper.grid(row=2,column=2)
scisscor.grid(row=2,column=3)

#Indicators
player_indicator=Label(root,font=60,text="COMPUTER",bg="black",fg="white")
comp_indicator=Label(root,font=60,text="USER",bg="black",fg="white")
player_indicator.grid(row=0,column=3)
comp_indicator.grid(row=0,column=1)

#Update images
choices=["ROCK","PAPER","SCISSOR"]

#Update choices
def updateimages(x):
#for computer    
    comp_choice=choices[randint(0,2)]
    if comp_choice=="ROCK":
        comp_label.configure(image=rock_img)
    elif comp_choice=="SCISSOR":
        comp_label.configure(image=scissor_img)
    else:
        comp_label.configure(image=paper_img)        

#for user
    if x=="ROCK":
        user_label.configure(image=rock_img)
    elif x=="SCISSOR":
        user_label.configure(image=scissor_img)
    else:
        user_label.configure(image=paper_img)  

    checkwin(x,comp_choice)          

#Results
msg=Label(root,font=50,bg="black",fg="white")
msg.grid(row=3,column=2)

#update message
#We are changing the text of the message
def updatemessage(x):
    msg['text']=x

#upadte the  user score   
def updateuserscore():
    score=int(player_score["text"])
    score=score+1
    player_score["text"]=str(score)

def updatecompscore():
    score=int(comp_score["text"])
    score=score+1
    comp_score["text"]=str(score)

#Check the winning conditions
def checkwin(player,computer):
    if player==computer:
        updatemessage("It's a Tie")
    elif player=="ROCK":
        if computer=="PAPER":
            updatemessage("You Lose")
            updatecompscore()
        else:
            updatemessage("You Win")
            updateuserscore()
    elif player=="PAPER":
        if computer=="ROCK":
            updatemessage("You Win")
            updateuserscore()
        else:
            updatemessage("You Lose")
            updatecompscore()
    elif player=="SCISSOR":  
        if computer=="PAPER":
            updatemessage("You Win")
            updateuserscore()
        else:
            updatemessage("You Lose")
            updatecompscore()
    else:
        pass
        
root.mainloop()
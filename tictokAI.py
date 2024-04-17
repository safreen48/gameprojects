# HERE is the game that i developed on tkinter library and this make u to play against 
#the cpu...sure i can say that u can't beat this.

import tkinter as tk
from tkinter import messagebox
window=tk.Tk()
window.title("welcome to gaming world")
window.geometry("600x500")

b=[['','',''],
   ['','',''],
   ['','','']]
p=0
q=0


label=tk.Label(window,text="tic-tac-toe Game")
label.grid(row=0,column=0)
label=tk.Label(window,text="player 1 : X")
label.grid(row=1,column=0)
label=tk.Label(window,text="player 2 : O")
label.grid(row=2,column=0)

turn=1
def clicked1():
    global turn
    if btn1["text"]==" ":
        btn1["text"],b[0][0]='X','X'
        check()
        bestmove()

def clicked2():
    global turn
    if btn2["text"]==" ":
        btn2["text"],b[0][1]="X","X"
        check()
        bestmove()

def clicked3():
    global turn
    if btn3["text"]==" ":
        btn3["text"],b[0][2]="X","X"
        check()
        bestmove()

def clicked4():
    global turn
    if btn4["text"]==" ":
        btn4["text"],b[1][0]="X","X"
        check()
        bestmove()

def clicked5():
    global turn
    if btn5["text"]==" ":
        btn5["text"],b[1][1]="X","X"
        check()
        bestmove()

def clicked6():
    global turn
    if btn6["text"]==" ":
        btn6["text"],b[1][2]="X","X"
        check()
        bestmove()

def clicked7():
    global turn
    if btn7["text"]==" ":
        btn7["text"],b[2][0]="X","X"
        check()
        bestmove()

def clicked8():
    global turn
    if btn8["text"]==" ":
        btn8["text"],b[2][1]="X","X"
        check()
        bestmove()

def clicked9():
    global turn
    if btn9["text"]==" ":
        btn9["text"],b[2][2]="X","X"
        check()
        bestmove()
#calculating the best move
def bestmove():

    bestscore=-200
    for i in range(0,3):
        for j in range(0,3):
            #print(b)
            if b[i][j]=='':
                b[i][j]='O'
                score=minimax(b,0,False)
                b[i][j]=''
                if score>bestscore:
                    bestscore=score
                    #print(bestscore)
                    global p
                    global q
                    p=i  
                    q=j
                    
    b[p][q]='O'
    
    if(p+q==0):
        print(p+q)
        btn1["text"]="O"
    elif p+q==1 and p==0:
        btn2["text"]="O"
    elif p+q==2 and p==0:
        btn3["text"]="O"
    elif p+q==1 and p==1:
        btn4["text"]='O'
    elif p+q==2 and p==1:
        btn5["text"]='O'
    elif p+q==3 and p==1:
        btn6["text"]='O'
    elif p+q==2:
        btn7["text"]='O'
    elif p+q==3:
        btn8["text"]='O'
    elif p+q==4:
        btn9["text"]='O'
    check()
    
scores={'X':-10,'O':10,'tie':0}

#using minimax function
def minimax(b,depth,isMaximizing):
    result=check1()
    global scores
    if result !='':
        return scores[result]
    if isMaximizing:
        bestscore=-200
        for i in range(0,3):
            for j in range(0,3):
                if(b[i][j]==''):
                    b[i][j]='O'
                    score=minimax(b,depth+1,False)
                    b[i][j]=''
                    bestscore=max(score,bestscore)
        return bestscore

    else:
        bestscore=200 
        for i in range(0,3):
            for j in range(0,3):
                if(b[i][j]==''):
                    b[i][j]='X'
                    score=minimax(b,depth+1,True)
                    b[i][j]=''
                    bestscore=min(score,bestscore)               
        return bestscore          

flag=1
def check():
    global flag
    winner=''
    openspots=0
    b1=btn1["text"]
    b2=btn2["text"]
    b3=btn3["text"]
    b4=btn4["text"]
    b5=btn5["text"]
    b6=btn6["text"]
    b7=btn7["text"]
    b8=btn8["text"]
    b9=btn9["text"]
    flag=flag+1
    if b1==b2 and b1==b3 and b1=="O" or b1==b2 and b1==b3 and b1=="X":    
        win(btn1["text"])
    if b4==b5 and b4==b6 and b4=="O" or b4==b5 and b4==b6 and b4=="X":
        win(btn4["text"])
    if b7==b8 and b7==b9 and b7=="O" or b7==b8 and b7==b9 and b7=="X":
        win(btn7["text"])
    if b1==b4 and b1==b7 and b1=="O" or b1==b4 and b1==b7 and b1=="X":
        win(btn1["text"])
    if b2==b5 and b2==b8 and b2=="O" or b2==b5 and b2==b8 and b2=="X":
        win(btn2["text"])
    if b3==b6 and b3==b9 and b3=="O" or b3==b6 and b3==b9 and b3=="X":
        win(btn3["text"])
    if b1==b5 and b1==b9 and b1=="O" or b1==b5 and b1==b9 and b1=="X":
        win(btn5["text"])
    if b3==b5 and b3==b7 and b3=="O" or b3==b5 and b3==b7 and b3=="X":
        win(btn5["text"])
    if flag==10:
        ans1="match is tied!!.....try again"
        messagebox.showinfo("sorry",ans1)
        window.destroy()

def check1():
    winner=''
    for i in range(0,3):
        if (b[i][0]==b[i][1]==b[i][2]=='X' or b[i][0]==b[i][1]==b[i][2]=='O'):
            winner=b[i][0]
    for i in range(0,3):
        if (b[0][i]==b[1][i]==b[2][i]=='X' or b[0][i]==b[1][i]==b[2][i]=='O'):
            winner=b[0][i]
    if (b[0][0]==b[1][1]==b[2][2]=='X' or b[0][0]==b[1][1]==b[2][2]=='O'):
        winner=b[0][0]
    if (b[2][0]==b[1][1]==b[0][2]=='X' or b[2][0]==b[1][1]==b[0][2]=='O'):
        winner=b[2][0]
    open=0
    for i in range(0,3):
        for j in range(0,3):
            if b[i][j]=='':
                open=open+1
    if winner=='' and open==0:
        return 'tie'
    else:
        return winner

def win(player):
    ans="game  complete  " +player+ " wins"
    messagebox.showinfo("congratulations ",ans)
    window.destroy()
#creating the buttons  and placing them in order
btn1=tk.Button(window,text=" ",bg="black",fg="red",width=9,height=4,font=('Helvetica','20'),command=clicked1)
btn2=tk.Button(window,text=" ",bg="black",fg="red",width=9,height=4,font=('Helvetica','20'),command=clicked2)
btn3=tk.Button(window,text=" ",bg="black",fg="red",width=9,height=4,font=('Helvetica','20'),command=clicked3)
btn4=tk.Button(window,text=" ",bg="black",fg="red",width=9,height=4,font=('Helvetica','20'),command=clicked4)
btn5=tk.Button(window,text=" ",bg="black",fg="red",width=9,height=4,font=('Helvetica','20'),command=clicked5)
btn6=tk.Button(window,text=" ",bg="black",fg="red",width=9,height=4,font=('Helvetica','20'),command=clicked6)
btn7=tk.Button(window,text=" ",bg="black",fg="red",width=9,height=4,font=('Helvetica','20'),command=clicked7)
btn8=tk.Button(window,text=" ",bg="black",fg="red",width=9,height=4,font=('Helvetica','20'),command=clicked8)
btn9=tk.Button(window,text=" ",bg="black",fg="red",width=9,height=4,font=('Helvetica','20'),command=clicked9)

btn1.grid(row=1,column=1)
btn2.grid(row=1,column=2)
btn3.grid(row=1,column=3)
btn4.grid(row=2,column=1)
btn5.grid(row=2,column=2)
btn6.grid(row=2,column=3)
btn7.grid(row=3,column=1)
btn8.grid(row=3,column=2)
btn9.grid(row=3,column=3)

window.mainloop()
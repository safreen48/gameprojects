import turtle
import time
#from tkinter import messagebox

delay=0.02

wn=turtle.Screen()
wn.title("flappy turtle by @arun pandyan")
wn.bgcolor("blue")
wn.bgpic("tictol.GIF")
wn.setup(width=600,height=700)
wn.tracer(0) 

player=turtle.Turtle()
player.speed(0)
player.shape("turtle")
player.color("red")
#player.shapesize(stretch_wid=0,stretch_len=0)
player.penup()
player.goto(-260,0)
player.dx=0
player.dy=1
gravity=-0.1

#block building
block1_top=turtle.Turtle()
block1_top.speed(0)
block1_top.shape("square")
block1_top.color("green")
block1_top.shapesize(stretch_wid=25,stretch_len=2)
block1_top.penup()
block1_top.goto(-130,340)
block1_top.dx=-2
block1_top.dy=0


block1_bot=turtle.Turtle()
block1_bot.speed(0)
block1_bot.shape("square")
block1_bot.color("green")
block1_bot.shapesize(stretch_wid=25,stretch_len=2)
block1_bot.penup()
block1_bot.goto(-130,-340)
block1_bot.dx=-2
block1_bot.dy=0

block2_top=turtle.Turtle()
block2_top.speed(0)
block2_top.shape("square")
block2_top.color("green")
block2_top.shapesize(stretch_wid=35,stretch_len=2)
block2_top.penup()
block2_top.goto(60,340)
block2_top.dx=-2
block2_top.dy=0


block2_bot=turtle.Turtle()
block2_bot.speed(0)
block2_bot.shape("square")
block2_bot.color("green")
block2_bot.shapesize(stretch_wid=35,stretch_len=2)
block2_bot.penup()
block2_bot.goto(250,-340)
block2_bot.dx=-2
block2_bot.dy=0


def go_up():
    player.dy+=3

wn.listen()
wn.onkeypress(go_up,"space")


while True:

   

    wn.update()

    

    player.dy+=gravity
    #player movement
    y=player.ycor()
    y+=player.dy
    player.sety(y)

    #blocks movement
    x=block1_top.xcor()
    x+=block1_top.dx
    block1_top.setx(x)
    
    x=block1_bot.xcor()
    x+=block1_bot.dx
    block1_bot.setx(x)

    x=block2_top.xcor()
    x+=block2_top.dx
    block2_top.setx(x)
    
    x=block2_bot.xcor()
    x+=block2_bot.dx
    block2_bot.setx(x)
    

    #collision conditions

    if block1_top.xcor()<-300:
        block1_top.setx(300)
        block1_bot.setx(300)

    if block2_top.xcor()<-300:
        block2_top.setx(300)
    
    if block2_bot.xcor()<-300:
        block2_bot.setx(300)

    if player.ycor()>340:
        ans="game overrrr"
        #messagebox.showinfo("congratulations ",ans) 
        #wn.destroy()
    if (player.xcor()+10>block1_top.xcor()-30) and (player.xcor()-10<block1_top.xcor()+30):
        if (player.ycor()+10>block1_top.ycor()-250) or (player.ycor()-10<block1_bot.ycor()+250):
           ans="game overrrr"
           #messagebox.showinfo("congratulations ",ans)
           #wn.destroy()
    

    
    time.sleep(delay)
   

wn.mainloop()

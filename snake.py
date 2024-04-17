import turtle
import time
import random

delay=0.1

score=0
high_score=0

wn=turtle.Screen()
wn.title("snake game......")
wn.bgcolor("black")
wn.setup(width=700,height=600)
wn.tracer(0)

#snake head

head=turtle.Turtle()
head.speed(0)
head.color("red")
head.shape("square")
head.goto(0,0)
head.penup()
head.direction="stop"

#food
food=turtle.Turtle()
food.speed(0)
food.color("green")
food.shape("circle")
food.penup()
food.goto(-100,0)

segments=[]

#pen

pen=turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("score : 0   High score : 0",align="center",font=("courier",24,"normal"))

# functions

def go_up():
    if head.direction !="down":
        head.direction="up"

def go_down():
    if head.direction !="up":
        head.direction="down"

def go_right():
    if head.direction !="left":
        head.direction="right"

def go_left():
    if head.direction !="right":
        head.direction="left"

def move():
    if head.direction=="up":
        head.sety(head.ycor()+20)

    if head.direction=="down":
        head.sety(head.ycor()-20)

    if head.direction=="right":
        head.setx(head.xcor()+20)

    if head.direction=="left":
        head.setx(head.xcor()-20)
        
# keyboard bindings
wn.listen()
wn.onkeypress(go_up,"w")
wn.onkeypress(go_down,"s")
wn.onkeypress(go_right,"d")
wn.onkeypress(go_left,"a")




#main loop
while True:
    wn.update()

    # body collison check
    if head.xcor()>340 or head.xcor()<-340 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1)
        head.goto(0,0)
        head.direction="stop"

        #hide of segments
        for segment in segments:
            segment.goto(100,1000)

        segments.clear()

        score=0
        
        pen.clear()
        pen.write("score : {}   High score : {}".format(score,high_score),align="center",font=("courier",24,"normal"))        

    if head.distance(food)<20:
        x=random.randint(-340,340)
        y=random.randint(-290,290)
        food.goto(x,y)

        new_segment=turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("white")
        new_segment.penup()
        segments.append(new_segment)

        score +=1
 
 
        if score > high_score:
            high_score=score
        
        pen.clear()
        pen.write("score : {}   High score : {}".format(score,high_score),align="center",font=("courier",24,"normal"))        

    for index in range(len(segments)-1,0,-1):
        x=segments[index-1].xcor()
        y=segments[index-1].ycor()
        segments[index].goto(x,y)

    if len(segments)>0:
        x=head.xcor()
        y=head.ycor()
        segments[0].goto(x,y)


    move()

    for segment in segments:
        if segment.distance(head)<20:
            time.sleep(1)
            head.goto(0,0)
            head.direction="stop"
            #hide of segments
            for segment in segments:
                segment.goto(100,1000)

            segments.clear()
            
            score=0

            pen.clear()
            pen.write("score : {}   High score : {}".format(score,high_score),align="center",font=("courier",24,"normal"))        


    time.sleep(delay)


wn.mainloop()
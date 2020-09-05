from turtle import*
import tkinter as tk
import time


#Defines the ask function

def ask():
    global MAX_SCORE
    MAX_SCORE = tk.simpledialog.askinteger("Input Field", "Score To Win", minvalue=1, maxvalue=80)
    MAX_SCORE = int(MAX_SCORE)

wn = Screen()

wn.title("PONG")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)
screen = wn.getcanvas()
start = 0
p1, p2 = 0, 0
sy = 0
ballRadius = 10
paddleHeight = 50
paddleWidth = 10
streak = 1.2
status = ""
MAX_SCORE = 0
draw = False
AI_Speed, skill = 1.2, 1
#Paddle A
p_a = Turtle()
p_a.speed(0)
p_a.shape("square")
p_a.color("white")
p_a.penup()
p_a.shapesize(stretch_wid=5, stretch_len=1)
p_a.goto(-350, 0)

def reset():
    p_b.sety(0)
    p_a.sety(0)
    time.sleep(0.025)

#Paddle B
p_b = Turtle()
p_b.speed(0)
p_b.shape("square")
p_b.color("white")
p_b.penup()
p_b.shapesize(stretch_wid=5, stretch_len=1)
p_b.goto(350, 0)

# Ball
ball = Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx, ball.dy = 2.1, 2.1
    
#Write Turtle
wt = Turtle()
wt.speed(0)
wt.shape("square")
wt.hideturtle()
wt.penup()

wt.color('White')
wt.write("{}    {}".format(p1, p2), align = "center", font = ("Pixel", 24, "normal"))


#Turtles
w = Turtle()
w.speed(0)
w.shape("square")
w.hideturtle()
w.penup()
wt.goto(0,235)
w.color('White')



#Line Turtle
turtle = Turtle()
turtle.speed(0)
turtle.shape("square")
turtle.penup()
turtle.goto(0, 276)
turtle.color("White")
turtle.shapesize(stretch_wid=0.78, stretch_len = 0.78)

for i in range(54):
    turtle.stamp()
    turtle.sety(turtle.ycor() - 28)



#Tells to start
def starter(event):
    global starter, start
    if not(start):
        start = 1
        ask()
        


"""Enemy AI movements"""

#Changes p_b's ycor
def Change(s):
    y = p_b.ycor()
    y += s
    for i in range(12):

        p_b.sety(p_b.ycor() + (y - p_b.ycor()))


#main AI

def AI():
    global AI_Speed, skill, streak
    if start:
        if not((p_b.xcor() -  ball.xcor()) < 180) and ball.dx < 0:
            p_b.sety(p_b.ycor() + (0 - p_b.ycor())/24)
        elif (p_b.xcor() - ball.xcor()) < 280:
            try:
                skill = (1.4 + (p_b/p_a)/5 * 4)
            except:
                if p2 + p1 == 0:
                    skill = 2
                elif p2 == 0:
                    skill = 3.1
                else:
                    skill = 3
            AI_Speed = skill*streak
            if AI_Speed < 1.2:
                AI_Speed = 1.4
            distance = ball.ycor() - p_b.ycor()
            if(ball.dx > 0):
                Change(0.8 * (distance * AI_Speed * 1.2) / 28)

            distance *= 0.9


    wn.ontimer(AI, 27)
               



"""Mouse Y Motion"""
#Collects Data
def Motion(event):
    global sy
    if (start):
        sy = ((event.y*-1)+300)
    else:
        sy = (p_a.ycor()) * -1
        

#Sets Y position to data from Motion(event)
def SetY():
    p_a.sety(p_a.ycor() + ((sy - p_a.ycor())/12))
    wn.ontimer(SetY, 10)


#Binding
screen.bind("<Motion>", Motion)
SetY()

#AI
AI()

#Game Loop 

while True:

    wn.update()

    """Starts Program"""
    if (start):
        #win
        if p1 > MAX_SCORE or p2 > MAX_SCORE:
            start = 0
            if p1 > p2:
                status = "WIN           LOSE"
            elif p2 > p1:
                status = "LOSE          WIN"

        else:
            #Sets ball positions

            ball.setx(ball.xcor() + ball.dx)
            ball.sety(ball.ycor() + ball.dy)

            """Border Check"""
            
            #Y Check
            if ball.ycor() > 290:

                ball.sety(285)
                ball.dy *= -1
            elif ball.ycor() < -290:
                ball.sety(-285)
                ball.dy *= -1
            
            #X Check
            if ball.xcor() > 390:
                reset()


                ball.goto(330, 0)

                ball.dx *=  -1
                p1 += 1
                streak += 0.5
                
                time.sleep(0.25)

            elif ball.xcor() < -390:
                reset()

                ball.goto(-330, 0)
                ball.dx *= -1
                p2 += 1
                streak -= 0.2

                time.sleep(0.25)

            #P2 Collision
            if (ball.xcor() > 340) and (ball.xcor() < 350) and (ball.ycor() < p_b.ycor() + 60) and (ball.ycor() > p_b.ycor() - 60):
                ball.setx(330)
                ball.dx *=  -1
                
            #P1 Collision
            if (ball.xcor() > -350) and (ball.xcor() < -340)  and (ball.ycor() < p_a.ycor() + 60) and (ball.ycor() > p_a.ycor() - 60):
                ball.setx(-330)
                ball.dx *=  -1

            status = ""
            draw = 0

     
    else:
        screen.bind("<Button-1>", starter)



        
        ball.home()
        
        reset()
        p1, p2 = 0, 0
        sy = 0
        wt.hideturtle()

    #Prints Score
    wt.clear()

    wt.goto(0, 235)
    wt.write("{}    {}".format(p1, p2), align = "center", font = ("Courier", 24, "normal"))
    if draw == 0:
        w.clear()
        w.goto(0, 0)
        w.write(status, align = "center", font = ("Courier", 24, "normal"))

    #Streak
    if streak <= 0:
        streak = 0.1



mainloop()

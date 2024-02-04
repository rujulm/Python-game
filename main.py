import turtle
import random
import tkinter as tk
import time
from tkinter import messagebox

box=tk.Tk()
box.geometry("300x300")
messagebox.showinfo("Information","Welcome to Save the Turtle!\n\nSave the turtle from eating plastic and help it to reach its family to win the game\n\nNOTE:\n- Click to begin the game\n- Use the arrow keys to navigate the turtle\n-You lose a life every time the turtle collides with the rocks\n-The game will end if the turtle eats plastic")
box.destroy()
box.mainloop()

screen=turtle.Screen()
screen.setup(width=800,height=500)
screen.bgpic("game1-bg.gif")
screen.title("Save the Turtle!")
screen.addshape("turtle.gif")

t=turtle.Turtle()
t.shape("turtle.gif")
t.penup()
t.goto(-320,40)
t.direction="stop"

lives=3

plastic=[]
food=[]

display=turtle.Turtle()
display.speed(0)
display.color("red")
display.penup()
display.goto(0,220)
display.pendown()
display.write('Lives: {}'.format(lives),align='center',font=('Courier',20))
display.hideturtle()

screen.addshape("p1.gif")
screen.addshape("p2.gif")
screen.addshape("f1.gif")
screen.addshape("f2.gif")
screen.addshape("rocks.gif")
screen.addshape("t2.gif")

t2=turtle.Turtle()
t2.shape("t2.gif")
t2.penup()
t2.goto(290,150)

rocks=turtle.Turtle()
rocks.shape("rocks.gif")
rocks.goto(0,0)

for i in range(4):
 p1=turtle.Turtle()
 p1.shape("p1.gif")
 p1.penup()
 x=random.randint(-300,370)
 y=random.randint(-150,150)
 p1.setposition(x,y)
 plastic.append(p1)
  
 p2=turtle.Turtle()
 p2.shape("p2.gif")
 p2.penup()
 x=random.randint(-300,370)
 y=random.randint(-150,150)
 p2.setposition(x,y)
 plastic.append(p2)

for i in range(3):
 f1=turtle.Turtle()
 f1.shape("f1.gif")
 f1.penup()
 x=random.randint(-350,370)
 y=random.randint(-150,150)
 f1.setposition(x,y)
 food.append(f1)
  
 f2=turtle.Turtle()
 f2.shape("f2.gif")
 f2.penup()
 x=random.randint(-350,370)
 y=random.randint(-150,150)
 f2.setposition(x,y)
 food.append(f2)

def movement():
    if t.direction=="up":
        y=t.ycor()
        y+=3
        t.sety(y)
    
    elif t.direction=="down":
        y=t.ycor()
        y-=3
        t.sety(y)
        
    elif t.direction=="left":
        x=t.xcor()
        x-=3
        t.setx(x)
    
    elif t.direction=="right":
        x=t.xcor()
        x+=3
        t.setx(x)
        
def move_up():
    t.direction="up"
    
def move_down():
    t.direction="down"
    
def move_left():
    t.direction="left"

def move_right():
    t.direction="right"

def move():
  for p in plastic:
    x=p.xcor()
    x-= 3
    if x<-360:
      p.hideturtle()
      x=random.randint(-370,370)
      p.setx(x)
      p.showturtle()
    else:
      p.setx(x)
  for f in food:
    if f==f2:
      x=f.xcor()
      x-=2
      if x<-360:
        f.hideturtle()
        x=random.randint(-370,370)
        f.setx(x)
        f.showturtle()
      else:
        f.setx(x)

def you_win():
  window2=tk.Tk()
  window2.title('Save the Turtle!')
  window2.configure(background="black")
  window2.geometry("300x180")
  label=tk.Label(window2, text='YOU WIN!',fg="red",bg="black",font=('Courier',30))
  label.pack()
  b1=tk.Button(window2,text="Exit",fg="white",bg="green",command=close,font=24)
  b1.place(x=160,y=100)
  b2=tk.Button(window2,text="Play Again",fg="white",bg="green",command=start,font=24)
  b2.place(x=20,y=100)
  window2.mainloop()
  
def game_over():
  window=tk.Tk()
  window.title('Save the Turtle!')
  window.configure(background="black")
  window.geometry("250x150")
  label2=tk.Label(window, text='GAME OVER!',fg="yellow",bg="black",font=('Courier',30))
  label2.pack()
  b1=tk.Button(window,text="Exit",fg="white",bg="green",command=close,font=24)
  b1.place(x=160,y=100)
  b2=tk.Button(window,text="Play Again",fg="white",bg="green",command=start,font=24)
  b2.place(x=20,y=100)
  window.mainloop()
  
def food_collide():
  score=0
  for f in food:
    if t.distance(f)<20:
      f.hideturtle()
      
def plastic_collide():
  for p in plastic:
    if t.distance(p)<20:
      game_over()
      
def home():
  if t.distance(t2)<40:
    you_win()
    
def close():
  turtle.bye()

def start():
  t.goto(-320,40)
  lives=3
  display.clear()
  display.write('Lives: {}'.format(lives),align='center',font=('Courier',20))
  time.sleep(1)
  while True:
    screen.update()
    home()
    movement()
    move()
    food_collide()
    plastic_collide()
    if t.xcor()<-330 or t.xcor()>330 or t.ycor()>180 or t.ycor()<-180:
      lives-=1
      display.clear()
      display.write('Lives: {}'.format(lives),align='center',font=('Courier',20))
      time.sleep(1)
      t.goto(-320,40)
      
    if lives==0:
      game_over()
      
screen.listen()
screen.onkeypress(move_up,"Up")
screen.onkeypress(move_down,"Down")
screen.onkeypress(move_left,"Left")
screen.onkeypress(move_right,"Right")


while True:
  screen.update()
  
  movement()
  move()
  plastic_collide()
  food_collide()
  home()
  if t.xcor()<-330 or t.xcor()>330 or t.ycor()>160 or t.ycor()<-160:
    lives-=1
    display.clear()
    display.write('Lives: {}'.format(lives),align='center',font=('Courier',20))
    time.sleep(1)
    t.goto(-320,40)
  if lives==0:
    game_over()
     
      
screen.exitonclick()
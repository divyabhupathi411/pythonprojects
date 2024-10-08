import turtle
import random
box = turtle.Turtle()
screen = turtle.Screen()
score = turtle.Turtle()
score1 = 0

screen.bgcolor("black")

box.speed(0)
box.penup()
box.goto(-200,125)
box.pendown()
box.color("red")
for i in range(4):
  box.forward(250)
  box.right(90)

score.penup()
score.goto(-200,135)
score.color("white")

t = turtle.Turtle()
t.penup()
t.goto(-75,0)
t.color("blue")
t.shape("turtle")
def right():
  t.right(10)
def left():
  t.left(10)
screen.onkey(right,"Right")
screen.onkey(left,"Left")
screen.listen()

turtles = []

for i in range(10):
  ball = turtle.Turtle()
  ball.speed(0)
  ball.color("red")
  ball.shape("circle")
  x = random.randint(-200,50)
  y = random.randint(-125,125)
  ball.penup()
  ball.goto(x,y)
  ball.speed(1000)
  turn = random.randint(0,360)
  ball.right(turn)
  turtles.append(ball)
  
def check(tur):
  if tur.xcor() < -200:
    tur.speed(0)
    tur.right(180)
    tur.speed(3)
  elif tur.xcor() > 50 :
    tur.speed(0)
    tur.right(180)
    tur.speed(3)
  elif tur.ycor() < -125 :
    tur.speed(0)
    tur.right(180)
    tur.speed(3)
  elif tur.ycor() > 125 :
    tur.speed(0)
    tur.right(180)
    tur.speed(3)
  
while True:
  for ball in turtles:
    ball.forward(10)
    check(ball)
    if abs(ball.xcor() - t.xcor()) < 10 and abs(ball.ycor() - t.ycor()) < 20:
      ball.ht()
      ball.goto(250,250)
      score1 = score1 + 1
      score.clear()
      score.write("score:"+str(score1))
  t.forward(15)
  check(t)







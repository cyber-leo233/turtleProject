from turtle import Turtle, Screen
import random

t = Turtle()
t.shape('turtle')
t.color('green')
t.pensize(10)
t.speed("fastest")




def random_color():
  r = random.randint(0, 255)
  g = random.randint(0, 255)
  b = random.randint(0, 255)
  color = (r, g, b)
  return color

# def random_speed():
#     speeds = [0, 1, 3, 6, 10]
#     return random.choice(speeds)


directions = [0, 90, 180, 270]

for _ in range(200):

    t.color(random_color())
    t.fd(50)
    t.setheading(random.choice(directions))

s = Screen()
s.exitonclick()

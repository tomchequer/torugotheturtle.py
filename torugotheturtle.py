import turtle as t
import random

torugo = t.Turtle()

torugo.shape('turtle')

t.colormode(255)

def actualgenrandcolor():
    return (random.randint(0, 255),random.randint(0, 255),random.randint(0, 255))

#def randomwalk(walks):
    for i in range(walks):
        torugo.speed(random.randint(1,6))
        torugo.pensize(random.randint(5, 15))
        torugo.setheading(randomangle())
        #torugo.right(random.randint(0,360))
        torugo.forward(random.randint(1, 50))
        torugo.color(actualgenrandcolor())

torugo.pensize(2)
torugo.speed('fastest')


def drawcircle(size):
    for i in range (int(360 / size)):
        torugo.color(actualgenrandcolor())
        torugo.circle(100)
        torugo.setheading(torugo.heading() + size)


drawcircle(4)

display = t.Screen()
display.exitonclick()


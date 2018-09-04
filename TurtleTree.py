# exercise from data structure in python
# recursive/tree

from turtle import *


def tree(branchLen,t):
    if branchLen >5:
        t.forward(branchLen)
        t.right(20)
        tree(branchLen-15,t)
        t.left(40)
        tree(branchLen-10,t)
        t.right(20)
        t.backward(branchLen)

t = Turtle()
myWindow = t.getscreen()
t.left(90) # move the position of the cursor
t.up()
t.backward(300)
t.down()
t.color('green') # set the color of the drawing path
tree(50,t)
myWindow.exitonclick()

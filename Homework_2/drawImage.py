__author__ = 'Pratik'

import turtle
import math


TOTAL_WOOD = 550
'''
    xcor = right wall of house
    ycor = height of tree + 30 + 30
    height of tree = max trunk length + head
'''
def draw_star(xcor, ycor):
    turtle.up()
    turtle.setposition(xcor, ycor+40)
    turtle.down()
    for x in range(0, 8):
        turtle.forward(30)
        turtle.back(30)
        turtle.left(45)
    turtle.up()


def draw_sun(xcor, ycor):
    turtle.up()
    turtle.setposition(xcor, ycor)
    turtle.down()
    turtle.circle(60)
    turtle.up


def draw_house(wallSize):
    turtle.down()
    turtle.forward(wallSize)
    turtle.left(90)
    turtle.forward(wallSize)
    maxX = turtle.xcor()
    turtle.left(45)
    turtle.forward(wallSize / math.sqrt(2))
    maxY = turtle.ycor()
    turtle.left(90)
    turtle.forward(wallSize / math.sqrt(2))
    turtle.left(45)
    turtle.forward(wallSize)
    turtle.left(90)
    turtle.forward(wallSize + 100)
    turtle.up()
    return maxX, maxY


def calculate_wall_size(total_wood):
    return total_wood / (2 + math.sqrt(2))


if __name__ == "__main__":
    x, y = draw_house(calculate_wall_size(TOTAL_WOOD))
    draw_sun(x, y + 20)
    draw_star(200, 200)
    turtle.done()

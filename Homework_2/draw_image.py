__author__ = 'kmd1712'
import turtle
import random
import math

totalWood = 0
maxHeight = 0


def init():
    global totalWood
    global maxHeight
    trees = int(input("How many trees in your forest?"))
    house = input("Is there a house in the forest (y/n)?")
    turtle.penup()
    turtle.setposition(-330, -100)
    if(trees < 2 and house == "y"):
        print("we need atleast two trees for drawing house")
        turtle.done()
    else:
        position_of_house = random.randint(1, trees - 1)
        counter = 1
        house_drawn = 0
        while counter <= trees :
            if counter - 1 == position_of_house and house_drawn == 0:
                y = drawHouse(100)
                house_drawn = 1
                totalWood = totalWood + y
                spaceBetween(counter, trees)
            else:
                type_of_tree = random.randint(1, 3)
                wood, height = drawTrees(type_of_tree)
                spaceBetween(counter, trees)
                totalWood = totalWood + wood
                counter = counter + 1
                if height > maxHeight:
                    maxHeight = height

    turtle.penup()
    draw_star(maxHeight)
    turtle.hideturtle()
    input("Press enter to exit")

def draw_star(ycor):
    turtle.up()
    turtle.left(90)
    turtle.forward(ycor+40)
    turtle.down()
    for x in range(0, 8):
        turtle.forward(30)
        turtle.back(30)
        turtle.left(45)
    turtle.up()


def drawHouse(wallSize):
        turtle.pendown()
        turtle.left(90)
        turtle.forward(wallSize)
        turtle.right(45)
        turtle.forward(50*(2**.5))
        turtle.right(90)
        turtle.forward(50*(2**.5))
        turtle.right(45)
        turtle.forward(wallSize)
        turtle.left(90)
        turtle.back(wallSize)
        turtle.forward(wallSize)
        return 2 * (wallSize + wallSize / math.sqrt(2))

def spaceBetween(treenumber,totaltree):

    if treenumber <= totaltree + 1:
        turtle.forward(100)
    turtle.penup()


def drawTrees (type_of_tree):
    if type_of_tree == 1:
        trunk = random.randint(50, 200)
        height = drawPine(trunk)

    elif type_of_tree == 2:
        trunk = random.randint(50, 150)
        height = drawMaple(trunk)

    else:
        trunk = random.randint(50, 100)
        height = drawMyTree(trunk)

    return trunk,height

def drawMyTree(trunk):
    drawTrunk(trunk)
    turtle.right(60)
    turtle.forward(30)
    turtle.left(60)
    turtle.forward(60)
    turtle.left(60)
    turtle.forward(30)
    turtle.left(60)
    turtle.forward(30)
    turtle.left(60)
    turtle.forward(60)
    turtle.left(60)
    turtle.forward(30)
    turtle.right(60)
    turtle.forward(trunk)
    turtle.left(90)
    height = trunk + (30 * (3 ** .5) + 60)
    return height

def drawMaple(trunk):
    drawTrunk(trunk)
    turtle.penup()
    turtle.right(90)
    turtle.forward(40)
    turtle.left(90)
    turtle.forward(40)
    turtle.pendown()
    turtle.circle(40)
    turtle.penup()
    turtle.back(trunk+40)
    turtle.right(90)
    turtle.back(40)
    turtle.pendown()
    height = trunk + 80
    return height


def drawPine(trunk):
    drawTrunk(trunk)
    turtle.left(90)
    turtle.forward(35)
    turtle.right(120)
    turtle.forward(70)
    turtle.right(120)
    turtle.forward(70)
    turtle.right(120)
    turtle.forward(35)
    turtle.left(90)
    turtle.forward(trunk)
    turtle.left(90)
    height = trunk + (3**.5)*35
    return height

def drawTrunk(trunk):
    turtle.pendown()
    turtle.left(90)
    turtle.forward(trunk)

if __name__ == '__main__':
    init()

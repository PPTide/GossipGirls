import math
import turtle
from FurnitureTurtle import *
from raum import *

from globals import *


def Pos(x, y):
    turtle.penup()
    turtle.setpos(x, y)
    turtle.pendown()


def eimer():
    Pos(-500, -200)
    turtle.right(85)
    turtle.forward(70)
    turtle.left(85)
    turtle.forward(40)
    turtle.left(85)
    turtle.forward(70)


eimer()

selected = -1
5400

turtle.getscreen().screensize(1280, 720)

drawRoom()


def dist(x1, y1, x2, y2):
    """
    Get the distance between 2 points

    :param x1:
    :param y1:
    :param x2:
    :param y2:
    :return:
    """
    xdist = math.fabs(x1 - x2)
    ydist = math.fabs(y1 - y2)
    return math.sqrt(xdist * xdist + ydist * ydist)


t1 = FurnitureTurtle()

t1.color("blue")
t1.setDrawFunc(
    createFurniture(
        "Bett",
        [
            (-50, 25),
            (50, 25),
            (50, -25),
            (-50, -25),
            (-50, 25),
        ],
        namePos=(0, 0),
    )
)
turtles.append(t1)

# t1.move(-20, -20)
t1.move(-300, -250, True)

t2 = FurnitureTurtle()

t2.color("blue")
t2.setDrawFunc(
    createFurniture(
        "Schrank",
        [
            (-40, 20),
            (40, 20),
            (40, -20),
            (-40, -20),
            (-40, 20),
        ],
        namePos=(0, 0),
    )
)
t2.move(-100, 0, True)
turtles.append(t2)

# t2.move(20, 20)
t2.move(-200, -250, True)

t3 = FurnitureTurtle()

t3.color("blue")
t3.setDrawFunc(
    createFurniture(
        "Stuhl",
        [
            (-15, 15),
            (15, 15),
            (15, -15),
            (-15, -15),
            (-15, 15),
        ],
        namePos=(0, 0),
    )
)
t3.move(-300, 0, True)
turtles.append(t3)

# t3.move(-20, -20)
t3.move(50, -250, True)

t4 = FurnitureTurtle()

t4.color("blue")
t4.setDrawFunc(
    createFurniture(
        "Kühlschrank",
        [(-20, 20), (-20, -20), (20, -20), (20, 20), (-20, 20)],
        namePos=(0, 0),
    )
)
t4.move(-300, 0)
turtles.append(t4)

# t4.move(-20, -20)
t4.move(0, -250, True)

t = FurnitureTurtle()

t.color("blue")
t.setDrawFunc(
    createFurniture(
        "Tisch",
        [
            (-40, 80),
            (40, 80),
            (40, -80),
            (-40, -80),
            (-40, 80),
        ],
        namePos=(0, 0),
    )
)
t.move(-300, 0, True)
turtles.append(t)

# t.move(-20, -20)
t.move(-100, -250, True)

tuerenUndFenster()


def cloneTurtleAndSelect(t):
    """
    Clones the turtle passed into this function and selects it"""
    global turtles
    global selected
    newTurtle = FurnitureTurtle()
    newTurtle.setDrawFunc(t.drawFunc)
    newTurtle.color("red")
    newTurtle.move(t.baseX, t.baseY, True)
    turtles.append(newTurtle)
    selected = len(turtles) - 1


def onClick(x, y):
    global selected
    global turtles
    """
Funktion to call on click

:param x:
:param y:
:return:
"""
    if selected == -1:
        # No Turtle is currently selected -> select a turtle by distance
        closest: FurnitureTurtle = None
        distClosest = math.inf
        for i, t in enumerate(turtles):
            # Go through each turtle keep the turtle that was closest to the click at that point and replace it if
            # the current turtle is closer
            distCurrent = dist(t.baseX, t.baseY, x, y)
            if distCurrent < distClosest:
                closest = t
                distClosest = distCurrent
                selected = i

        if (
            selected <= 4
        ):  # Wählt nur die Objekte aus, die sich als erste oder als zweites im Programm befinden
            cloneTurtleAndSelect(closest)
        else:
            closest.color("red")  # Color the turtle red -> the item red
            closest.move(
                closest.baseX, closest.baseY
            )  # move it to the position it was already at to redraw with the new color
    else:
        # Code used to delete furniture

        # Wenn im Müll bereich geklick wurde ->
        #   Lösche das Möbelstück
        if x <= -400 and y <= -150:
            turtles[selected].clear()
            del turtles[selected]
            selected = -1

        else:
            turtles[selected].move(x, y)


def onESC():
    global selected
    global turtles

    t = turtles[selected]
    t.color("black")
    t.move(t.baseX, t.baseY)
    selected = -1
    print("removed turtle selection")


def onRClick(x, y):
    global selected
    global turtles

    t = turtles[selected]
    # Rotate the turtle by 90 degrees
    t.rotation = (t.rotation + 90) % 360
    t.move(t.baseX, t.baseY)
    print("rotated turtle to " + str(t.rotation) + " degrees")


turtle.hideturtle()
turtle.getscreen().onclick(onClick)
turtle.getscreen().onclick(onRClick, 2)
turtle.getscreen().onkey(onESC, "Escape")
turtle.getscreen().onkey(onESC, "q")

turtle.listen()

turtle.mainloop()

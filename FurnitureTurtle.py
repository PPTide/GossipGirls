import math
import turtle

innerTopLeft = (-570, -145)
innerWidth = 790
innerHeight = 440


class FurnitureTurtle(turtle.Turtle):
    """
    Turtle used by this program which enables moving of the turtle
    """

    def __init__(self):
        """
        Initializes the turtle
        """
        super().__init__()
        self.drawFunc = None
        self.baseY = 0
        self.baseX = 0
        self.rotation = 90
        self.hitbox = ()
        self.getscreen().tracer(False)
        self.hideturtle()

    def setDrawFunc(self, func):
        """
        Set the function to call when drawing the shape

        :param func: function with which to draw the furniture item
        """
        self.drawFunc = func
        self.move(self.xcor(), self.ycor())

    def move(self, x, y, ignoreRoomBorder=False):
        """
        Move the shape set to the position x, y

        :param x: x position
        :param y: y position
        :param ignoreRoomBorder: if the furniture should be restricted within the room borders
        :return:
        """
        # Check if the furniture should be restricted within the room borders
        if not ignoreRoomBorder:
            # Iterate over each point in the furniture's hitbox to check if the furniture is out of the room's
            # boundaries
            for p in self.hitbox:
                if (
                    p[0] + x < innerTopLeft[0]
                    or p[1] + y < innerTopLeft[1]
                    or p[0] + x > innerTopLeft[0] + innerWidth
                    or p[1] + y > innerTopLeft[1] + innerHeight
                ):
                    # If the furniture is out of the room, show an error message and stop the function execution
                    turtle.TK.messagebox.showerror(
                        title="Out of bounds",
                        message="Das Möbelstück wurde außerhalb des Raums platziert",
                    )
                    return

        # Move the turtle to the new position, update the base coordinates, and clear the previous drawing
        self.goto(x, y)
        self.baseX = x
        self.baseY = y
        self.clear()

        # Check if a drawing function is set and is callable
        if not (self.drawFunc and callable(self.drawFunc)):
            turtle.TK.messagebox.showerror(
                title="Error", message="Error moving turtle have you set a draw function"
            )
            return

        # Set the turtle's heading to 0 degrees (east), call the drawing function, and update the screen to show the
        # new drawing
        self.setheading(0)
        self.drawFunc(self)
        self.getscreen().update()

    def addHitbox(self, hitbox):
        """
        Adds a hitbox to the Shape
        """
        self.hitbox = hitbox


def rotatePoint(p, rotation):
    """
    Rotates a point around the origin by the given rotation

    :param p: point to rotate
    :param rotation: rotation in degrees
    :return: rotated point
    """
    # Convert the rotation to radians
    rotation = math.radians(rotation-90)
    # Calculate the sine and cosine of the rotation
    sin = math.sin(rotation)
    cos = math.cos(rotation)
    # Rotate the point around the origin
    return (p[0] * cos - p[1] * sin, p[0] * sin + p[1] * cos)


def createFurniture(name, points, namePos=(0, 0)):
    """
    Returns a function to draw an item of furniture with name and points
    """

    def drawFunc(turtle: FurnitureTurtle):
        # Add hitbox to the turtle
        turtle.addHitbox(points)
        turtle.penup()
        # Rotate Points
        rotated_points = [(0,0) for _ in points]
        for i, p in enumerate(points):
            rotated_points[i] = rotatePoint(p, turtle.rotation)
        rotated_name_pos = rotatePoint(namePos, turtle.rotation)
        # Move to the position for the name and write the name
        turtle.goto(rotated_name_pos[0] + turtle.baseX, rotated_name_pos[1] + turtle.baseY)
        turtle.write(name, align="center")
        # Move to the first point of the shape
        turtle.goto(rotated_points[0][0] + turtle.baseX, rotated_points[0][1] + turtle.baseY)
        turtle.pendown()
        # Draw the shape by moving to each point in the list
        for p in rotated_points:
            turtle.goto(p[0] + turtle.baseX, p[1] + turtle.baseY)

    return drawFunc

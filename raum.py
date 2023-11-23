import turtle
import DoorAndWindow as dw
from globals import *

# es wird Variablen ein Wert/Koordinate zugeordnet
innerTopLeft = (-570, -145)  # es ist BottomLeft!!!
innerWidth = 790
innerHeight = 440

t = turtle.Turtle()

# es wird die Funktion getscreen an der Turtle abgerufen, um das Zeichnen zu entfernen
t.getscreen().tracer(False)
t.hideturtle()

# Raum wird gemalt
def drawRoom():
    t.penup()
    t.goto(-575, -150)
    t.pendown()
    for i in range(2):
        t.fd(800)
        t.lt(90)
        t.fd(450)
        t.lt(90)
    t.penup()
    t.goto(innerTopLeft)
    t.pendown()
    for i in range(2):
        t.fd(790)
        t.lt(90)
        t.fd(440)
        t.lt(90)
    # es wird alles vorherige direkt gemalt
    t.getscreen().update()

# eine Funktion für das Fenster malen wird erstellt
def fenster_malen(t):
  # die Farbe wird gleich einer Funktion gesetzt, damit diese sich variabler ändern kann
  color = t.color()
  # je nach Raumseite wird das Fenster in eine andere Richtung gemalt
  t.setheading(t.rotation)
  t.pendown()
  t.color("white")
  t.right(90)
  t.fd(40)
  t.right(90)
  t.color(color[0])
  t.fd(5)
  t.right(90)
  t.color("white")
  t.fd(80)
  t.right(90)
  t.color(color[0])
  t.fd(2.5)
  t.right(90)
  t.fd(80)
  t.right(180)
  t.fd(80)
  t.right(90)
  t.fd(2.5)
  t.right(90)
  t.color("white")
  t.fd(40)
  t.color(color[0])
  
# eine Funktion zum Malen von Türen wird erstellt
def tueren_malen(t):
  # die Farbe wird gleich einer Funktion gesetzt, damit diese sich variabler ändern kann
  color = t.color()
  # je nach Raumseite wird das Fenster in eine andere Richtung gemalt
  t.setheading(t.rotation)
  t.right(90)
  t.pendown()
  t.color("white")
  t.fd(40)
  t.right(180)
  t.fd(80)
  t.right(270)
  t.fd(5)
  t.right(270)
  t.fd(80)
  t.color(color[0])
  t.right(90)
  t.fd(7.5)
  t.right(180)
  t.fd(20)
  t.penup()
  t.right(270)
  t.fd(80)
  t.right(270)
  t.fd(20)
  t.pendown()
  t.right(180)
  t.fd(87.5)
  t.right(-90)
  t.circle(80, -90)

# eine Funktion zur Abfrage von dem Wunsch nach Türen und Fenstern wird gestartet
def tuerenUndFenster():
    anzahl_tueren = int(
        turtle.numinput("Türen", "Wie viele Türen willst du platzieren?")
    )
    if anzahl_tueren < 0:
        print("Nur positive Zahlen!!!")
        tuerenUndFenster()

    if anzahl_tueren > 0:
        for i in range(anzahl_tueren):
            tuer = dw.DoorAndWindowTurtle()
            tuer.setDrawFunc(tueren_malen)
            turtles.append(tuer)
            tuer.move(-100, -145)

    anzahl_fenster = int(
        turtle.numinput("Fenster", "Wie viele Fenster willst du platzieren?")
    )
    if anzahl_fenster >= 0:
        for i in range(anzahl_fenster):
            fenster = dw.DoorAndWindowTurtle()
            fenster.setDrawFunc(fenster_malen)
            turtles.append(fenster)
            fenster.move(0, -145)
    else:
        print("Nur positive Zahlen!!!")

    t.getscreen().update()
1

import FurnitureTurtle as ft
import turtle


class DoorAndWindowTurtle(ft.FurnitureTurtle):
    def move(self, x, y):
        if x < 180 and x > -530 and y < 150:
            y = -145
            self.rotation = 90
        elif x < 180 and x > -530 and y > 150:
            y = 295
            self.rotation = 270
        elif x < -530 and y > -105 and y < 255:
            x = -570
            self.rotation = 0
        elif x > 180 and y > -105 and y < 255:
            x = 220
            self.rotation = 180
        else:
          turtle.TK.messagebox.showerror(
              title="Out of bounds",
              message="Das Objekt wurde außerhalb des Raums platziert.",
          )
          return
        super().move(x, y)

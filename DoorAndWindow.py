import FurnitureTurtle as ft
import turtle


class DoorAndWindowTurtle(ft.FurnitureTurtle):
      # es wird eine Funktion erstellt, die guckt wo der Mauszeiger hin klickt und je nachdem das Objekt dreht und an an die Wand snapt
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
          # wenn es nicht im Raum platziert, öffnet ein Error Fenster
          turtle.TK.messagebox.showerror(
              title="Out of bounds",
              message="Das Objekt wurde außerhalb des Raums platziert.",
          )
          return
        super().move(x, y)

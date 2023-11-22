import FurnitureTurtle as ft


class DoorAndWindowTurtle(ft.FurnitureTurtle):
    def move(self, x, y):
        if x < 180 and x > -530 and y < 150:
            y = -147.5
            self.rotation = 90
        elif x < 180 and x > -530 and y > 150:
            y = 297.5
            self.rotation = 270
        elif x < -530 and y > -205 and y < 215:
            x = -612.5
            self.rotation = 0
        elif x > 180 and y > -205 and y < 215:
            x = 182.5
            self.rotation = 180
        super().move(x, y)

from imports import *

x, y = pyautogui.position()

dt = 0.1

class mousedata:
    def __init__(self, x, y, dt):
        self.x , self.y = pyautogui.position()
        self.dt = 0.1
    def velocity(x1, x2, y1, y2, dt):
        xcomp = (x2-x1)/dt
        ycomp = (y2-y1)/dt
        return xcomp, ycomp
    def speed(x1, x2, y1, y2, dt):
        xcomp = (x2-x1)/dt
        ycomp = (y2-y1)/dt
        speed = math.sqrt(xcomp**2 + ycomp**2)
        




from imports import *
x, y = pyautogui.position()

dt = 0.01

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
    def moveAndClick(x,y):
        pyautogui.moveTo(x,y)
        pyautogui.click(x,y)
        

"""while True:
    xinit, yinit = pyautogui.position()
    time.sleep(dt)
    xfin, yfin = pyautogui.position()
    print(mousedata.velocity(xinit, xfin, yinit, yfin, dt))
    print(xinit,  " " , yinit)"""
from imports import *
import mousedata

"""dt = 0.1

while True:
    xinit, yinit = pyautogui.position()
    time.sleep(dt)
    xfin, yfin = pyautogui.position()
    print(mousedata.velocity(xinit, xfin, yinit, yfin, dt))"""

ref_img = cv.imread("button_image.png")

"""if ref_img is None:
    sys.exit("no image")

cv.imshow("Display window", ref_img)
k = cv.waitKey(0)"""

ss = pyautogui.screenshot()
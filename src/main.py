from imports import *

if __name__ == "__main__":
    currentDir = os.path.dirname(__file__)
    imagesDir = os.path.join(currentDir, '../images')

    buttonImg1 = cv.cvtColor(cv.imread(os.path.join(imagesDir, 'button1.png')), cv.COLOR_BGR2GRAY)
    buttonImg2 = cv.cvtColor(cv.imread(os.path.join(imagesDir, 'button2.png')), cv.COLOR_BGR2GRAY)
    buttonImg3 = cv.cvtColor(cv.imread(os.path.join(imagesDir, 'button3.png')), cv.COLOR_BGR2GRAY)
    buttonImg4 = cv.cvtColor(cv.imread(os.path.join(imagesDir, 'button4.png')), cv.COLOR_BGR2GRAY)

    cv.waitKey(5) 

    try:
        while True:
            ss = pyautogui.screenshot("ss.png")
            screenImg = cv.cvtColor(cv.cvtColor(np.array(ss), cv.COLOR_RGB2BGR), cv.COLOR_BGR2GRAY)

            threshold = 0.9
            tolerence = 75

            minVal1, maxVal1, minLoc1, maxLoc1 = cv.minMaxLoc(cv.matchTemplate(screenImg, buttonImg1, cv.TM_CCOEFF_NORMED))
            minVal2, maxVal2, minLoc2, maxLoc2 = cv.minMaxLoc(cv.matchTemplate(screenImg, buttonImg2, cv.TM_CCOEFF_NORMED))
            minVal3, maxVal3, minLoc3, maxLoc3 = cv.minMaxLoc(cv.matchTemplate(screenImg, buttonImg3, cv.TM_CCOEFF_NORMED))
            minVal4, maxVal4, minLoc4, maxLoc4 = cv.minMaxLoc(cv.matchTemplate(screenImg, buttonImg4, cv.TM_CCOEFF_NORMED))


            if threshold <= maxVal1: 
                if (maxLoc1[0]- tolerence) <= pyautogui.position()[0] <= (maxLoc1[0] + buttonImg1.shape[1] + tolerence) and (maxLoc1[1] - tolerence) <= pyautogui.position()[1] <= (maxLoc1[0] + buttonImg1.shape[1] + tolerence):
                    pyautogui.moveTo((maxLoc1[0] + buttonImg1.shape[1]/2), (maxLoc1[1] + buttonImg1.shape[0]/2))
                pass

            elif threshold <= maxVal2: 
                if (maxLoc2[0]- tolerence) <= pyautogui.position()[0] <= (maxLoc2[0] + buttonImg2.shape[1] + tolerence) and (maxLoc2[1] - tolerence) <= pyautogui.position()[1] <= (maxLoc2[0] + buttonImg2.shape[1] + tolerence):
                    pyautogui.moveTo((maxLoc2[0] + buttonImg2.shape[1]/2), (maxLoc2[1] + buttonImg2.shape[0]/2))
                pass

            elif threshold <= maxVal3: 
                if (maxLoc3[0]- tolerence) <= pyautogui.position()[0] <= (maxLoc3[0] + buttonImg3.shape[1] + tolerence) and (maxLoc3[1] - tolerence) <= pyautogui.position()[1] <= (maxLoc3[0] + buttonImg3.shape[1] + tolerence):
                    pyautogui.moveTo((maxLoc3[0] + buttonImg3.shape[1]/2), (maxLoc3[1] + buttonImg3.shape[0]/2))
                pass

            elif threshold <= maxVal4: 
                if (maxLoc4[0]- tolerence) <= pyautogui.position()[0] <= (maxLoc4[0] + buttonImg4.shape[1] + tolerence) and (maxLoc4[1] - tolerence) <= pyautogui.position()[1] <= (maxLoc4[0] + buttonImg4.shape[1] + tolerence):
                    pyautogui.moveTo((maxLoc4[0] + buttonImg4.shape[1]/2), (maxLoc4[1] + buttonImg4.shape[0]/2))
                pass

            cv.destroyAllWindows()
            os.remove("ss.png")
            
    except KeyboardInterrupt:
        os.remove("ss.png")
        print("application closed")


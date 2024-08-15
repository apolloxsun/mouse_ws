from imports import *

if __name__ == "__main__":
    currentDir = os.path.dirname(__file__)
    imagesDir = os.path.join(currentDir, '../images')

    buttonImg1 = cv.cvtColor(cv.imread(os.path.join(imagesDir, 'button1.png')), cv.COLOR_BGR2GRAY)
    buttonImg2 = cv.cvtColor(cv.imread(os.path.join(imagesDir, 'button2.png')), cv.COLOR_BGR2GRAY)
    buttonImg3 = cv.cvtColor(cv.imread(os.path.join(imagesDir, 'button3.png')), cv.COLOR_BGR2GRAY)
    buttonImg4 = cv.cvtColor(cv.imread(os.path.join(imagesDir, 'button4.png')), cv.COLOR_BGR2GRAY)

    cv.waitKey(10)

    try:
        while True:
            ss = pyautogui.screenshot("ss")
            screenImg = cv.cvtColor(cv.cvtColor(np.array(ss), cv.COLOR_RGB2BGR), cv.COLOR_BGR2GRAY)

            threshold = 0.9

            minVal1, maxVal1, minLoc1, maxLoc1 = cv.minMaxLoc(cv.matchTemplate(screenImg, buttonImg1, cv.TM_CCOEFF_NORMED))
            minVal2, maxVal2, minLoc2, maxLoc2 = cv.minMaxLoc(cv.matchTemplate(screenImg, buttonImg2, cv.TM_CCOEFF_NORMED))
            minVal3, maxVal3, minLoc3, maxLoc3 = cv.minMaxLoc(cv.matchTemplate(screenImg, buttonImg3, cv.TM_CCOEFF_NORMED))
            minVal4, maxVal4, minLoc4, maxLoc4 = cv.minMaxLoc(cv.matchTemplate(screenImg, buttonImg4, cv.TM_CCOEFF_NORMED))


            if threshold <= maxVal1: 
                print("button1")
                if (maxLoc1[0]- 20) <= pyautogui.position()[0] <= (maxLoc1[0] + buttonImg1.shape[1] + 20) and (maxLoc1[1] - 20) <= pyautogui.position()[1] <= (maxLoc1[0] + buttonImg1.shape[1] + 20):
                    print("mouse in bounds")
                    pyautogui.moveTo((maxLoc1[0] + buttonImg1.shape[1]/2), (maxLoc1[1] + buttonImg1.shape[0]/2))
                else:
                    print("not in bounds")

            elif threshold <= maxVal2: 
                print("button2")
                if (maxLoc1[0]- 20) <= pyautogui.position()[0] <= (maxLoc1[0] + buttonImg2.shape[1] + 20) and (maxLoc1[1] - 20) <= pyautogui.position()[1] <= (maxLoc1[0] + buttonImg2.shape[1] + 20):
                    print("mouse in bounds")
                    pyautogui.moveTo((maxLoc1[0] + buttonImg2.shape[1]/2), (maxLoc1[1] + buttonImg2.shape[0]/2))
                else:
                    print("not in bounds")

            elif threshold <= maxVal3: 
                print("button3")
                if (maxLoc1[0]- 20) <= pyautogui.position()[0] <= (maxLoc1[0] + buttonImg3.shape[1] + 20) and (maxLoc1[1] - 20) <= pyautogui.position()[1] <= (maxLoc1[0] + buttonImg3.shape[1] + 20):
                    print("mouse in bounds")
                    pyautogui.moveTo((maxLoc1[0] + buttonImg3.shape[1]/2), (maxLoc1[1] + buttonImg3.shape[0]/2))
                else:
                    print("not in bounds")
                    print((maxLoc1[0] + buttonImg3.shape[1]/2), (maxLoc1[1] + buttonImg3.shape[0]/2))

            elif threshold <= maxVal4: 
                print("button4")
                if (maxLoc1[0]- 20) <= pyautogui.position()[0] <= (maxLoc1[0] + buttonImg4.shape[1] + 20) and (maxLoc1[1] - 20) <= pyautogui.position()[1] <= (maxLoc1[0] + buttonImg4.shape[1] + 20):
                    print("mouse in bounds")
                    pyautogui.moveTo((maxLoc1[0] + buttonImg4.shape[1]/2), (maxLoc1[1] + buttonImg4.shape[0]/2))
                else:
                    print("not in bounds")

            else:
                print("no button found")



            cv.waitKey(10)
            cv.destroyAllWindows()
            os.remove("ss")
            
    except KeyboardInterrupt:
        os.remove("ss")
        print("application closed")

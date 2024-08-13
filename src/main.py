from imports import *

if __name__ == "__main__":
    currentDir = os.path.dirname(__file__)
    imagesDir = os.path.join(currentDir, '../images')
    buttonPath1 = os.path.join(imagesDir, 'button1.png')
    buttonPath2 = os.path.join(imagesDir, 'button2.png')
    buttonPath3 = os.path.join(imagesDir, 'button3.png')
    buttonPath4 = os.path.join(imagesDir, 'button4.png')


    buttonImg1 = cv.cvtColor(cv.imread(os.path.join(imagesDir, 'button1.png')), cv.COLOR_BGR2GRAY)
    cv.waitKey(1000)

    try:
        while True:
            ss = pyautogui.screenshot()
            screenImg = cv.cvtColor(cv.cvtColor(np.array(ss), cv.COLOR_RGB2BGR), cv.COLOR_BGR2GRAY)

            score = cv.matchTemplate(screenImg, buttonImg1, cv.TM_CCOEFF_NORMED)
            #cv.imshow("score", cv.resize(screenImg, (800,600), interpolation=cv.INTER_AREA))

            threshold = 0.9

            minVal, maxVal, minLoc, maxLoc = cv.minMaxLoc(score)
            print(maxLoc)

            if threshold <= maxVal: print("yes")
            """printImg = cv.resize(screenImg, (800,600), interpolation=cv.INTER_AREA)
            cv.imshow("display" , printImg)"""

            cv.waitKey(10) 
            cv.destroyAllWindows()
            
    except KeyboardInterrupt:
        print("application closed")

    """threshold = 0.8
    location = np.where(score>=threshold)
    print(location)


    
    cv.waitKey(10000)"""
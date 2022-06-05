import time
import numpy as np
import cv2

def find_color(cam):
    width=640
    height=480
    roi_size = 400

    yellowLowValues = [25, 76, 101]
    yellowHighValues = [55, 255, 255]

    purpleLowValues = [102, 90, 121]
    purpleHighValues = [116, 255, 255]

    greenLowValues = [47, 35, 80]
    greenHighValues = [85, 201, 255]

    orangeLowValues = [10, 120, 120]
    orangeHighValues = [23, 255, 255]

    brownLowValues = [0, 0, 16]
    brownHighValues = [41, 108, 200]

    pinkLowValues = [121, 16, 109]
    pinkHighValues = [177, 243, 255]

    redLowValues = [0, 88, 118]
    redHighValues = [13, 248, 255]

    densities = [0,0,0,0,0,0,0]


    ret,  frame = cam.read()
    if ret:
        roi_img = frame[int((height - roi_size) / 2):int((height + roi_size) / 2),
                  int((width - roi_size) / 2):int((width + roi_size) / 2)]
        frameHSV=cv2.cvtColor(roi_img,cv2.COLOR_BGR2HSV)


        lowerBound=np.array(yellowLowValues)
        upperBound=np.array(yellowHighValues)
        yellowMask=cv2.inRange(frameHSV,lowerBound,upperBound)
        #cv2.imshow("yellow maks", yellowMask)
        densities[0] = (np.count_nonzero(yellowMask))

        lowerBound=np.array(purpleLowValues)
        upperBound=np.array(purpleHighValues)
        purpleMask=cv2.inRange(frameHSV,lowerBound,upperBound)
        #cv2.imshow("purpleMask", purpleMask)
        densities[1] = (np.count_nonzero(purpleMask))

        lowerBound=np.array(greenLowValues)
        upperBound=np.array(greenHighValues)
        greenMask=cv2.inRange(frameHSV,lowerBound,upperBound)
        #cv2.imshow("greenMask", greenMask)
        densities[2] = (np.count_nonzero(greenMask))

        lowerBound=np.array(orangeLowValues)
        upperBound=np.array(orangeHighValues)
        orangeMask=cv2.inRange(frameHSV,lowerBound,upperBound)
        #cv2.imshow("orangeMask", orangeMask)
        densities[3] = (np.count_nonzero(orangeMask))

        lowerBound=np.array(brownLowValues)
        upperBound=np.array(brownHighValues)
        brownMask=cv2.inRange(frameHSV,lowerBound,upperBound)
        #cv2.imshow("brownMask", brownMask)
        densities[4] = (np.count_nonzero(brownMask))

        lowerBound=np.array(pinkLowValues)
        upperBound=np.array(pinkHighValues)
        pinkMask=cv2.inRange(frameHSV,lowerBound,upperBound)
        #cv2.imshow("pinkMask", pinkMask)
        densities[5] = (np.count_nonzero(pinkMask))

        lowerBound=np.array(redLowValues)
        upperBound=np.array(redHighValues)
        redMask=cv2.inRange(frameHSV,lowerBound,upperBound)
        #cv2.imshow("redMask", redMask)
        densities[6] = (np.count_nonzero(redMask))

        #cv2.imshow('my WEBcam', frame)
        #cv2.moveWindow('my WEBcam', 0, 0)
        if cv2.waitKey(10) & 0xff == ord('q'):
            cv2.destroyAllWindows()
            cam.release()

        if max(densities) > 12000:
            if densities.index(max(densities)) == 0:
                print("yellow")
                print(densities[0])
                return "yellow"
            if densities.index(max(densities)) == 1:
                #if densities[4] > 12000:
                    #print("brown by purple")
                    #print(densities[4])
                    #return "brown"
                print("purple")
                print(densities[1])
                return "purple"
            if densities.index(max(densities)) == 2:
                print("green")
                print(densities[2])
                return "green"
            if densities.index(max(densities)) == 3:
                print("orange")
                print(densities[3])
                return "orange"
            if densities.index(max(densities)) == 4:
                print("brown")
                print(densities[4])
                return "brown"
            if densities.index(max(densities)) == 5:
                print("pink")
                print(densities[5])
                return "pink"
            if densities.index(max(densities)) == 6:
                print("red")
                print(densities[6])
                return "red"
        else:
            time.sleep(0.10)
            ret, frame = cam.read()
            if ret:
                roi_img = frame[int((height - roi_size) / 2):int((height + roi_size) / 2),
                          int((width - roi_size) / 2):int((width + roi_size) / 2)]
                frameHSV = cv2.cvtColor(roi_img, cv2.COLOR_BGR2HSV)

                lowerBound = np.array(yellowLowValues)
                upperBound = np.array(yellowHighValues)
                yellowMask = cv2.inRange(frameHSV, lowerBound, upperBound)
                #cv2.imshow("yellow maks", yellowMask)
                densities[0] = (np.count_nonzero(yellowMask))

                lowerBound = np.array(purpleLowValues)
                upperBound = np.array(purpleHighValues)
                purpleMask = cv2.inRange(frameHSV, lowerBound, upperBound)
                #cv2.imshow("purpleMask", purpleMask)
                densities[1] = (np.count_nonzero(purpleMask))

                lowerBound = np.array(greenLowValues)
                upperBound = np.array(greenHighValues)
                greenMask = cv2.inRange(frameHSV, lowerBound, upperBound)
                #cv2.imshow("greenMask", greenMask)
                densities[2] = (np.count_nonzero(greenMask))

                lowerBound = np.array(orangeLowValues)
                upperBound = np.array(orangeHighValues)
                orangeMask = cv2.inRange(frameHSV, lowerBound, upperBound)
                #cv2.imshow("orangeMask", orangeMask)
                densities[3] = (np.count_nonzero(orangeMask))

                lowerBound = np.array(brownLowValues)
                upperBound = np.array(brownHighValues)
                brownMask = cv2.inRange(frameHSV, lowerBound, upperBound)
                #cv2.imshow("brownMask", brownMask)
                densities[4] = (np.count_nonzero(brownMask))

                lowerBound = np.array(pinkLowValues)
                upperBound = np.array(pinkHighValues)
                pinkMask = cv2.inRange(frameHSV, lowerBound, upperBound)
                #cv2.imshow("pinkMask", pinkMask)
                densities[5] = (np.count_nonzero(pinkMask))

                lowerBound = np.array(redLowValues)
                upperBound = np.array(redHighValues)
                redMask = cv2.inRange(frameHSV, lowerBound, upperBound)
                #cv2.imshow("redMask", redMask)
                densities[6] = (np.count_nonzero(redMask))

                #cv2.imshow('my WEBcam', frame)
                #cv2.moveWindow('my WEBcam', 0, 0)
                if cv2.waitKey(10) & 0xff == ord('q'):
                    cv2.destroyAllWindows()
                    cam.release()

                if max(densities) > 12000:
                    if densities.index(max(densities)) == 0:
                        print("yellow")
                        print(densities[0])
                        return "yellow"
                    if densities.index(max(densities)) == 1:
                        #if densities[4] > 12000:
                            #print("brown by purple")
                            #print(densities[4])
                            #return "brown"
                        print("purple")
                        print(densities[1])
                        return "purple"
                    if densities.index(max(densities)) == 2:
                        print("green")
                        print(densities[2])
                        return "green"
                    if densities.index(max(densities)) == 3:
                        print("orange")
                        print(densities[3])
                        return "orange"
                    if densities.index(max(densities)) == 4:
                        print("brown")
                        print(densities[4])
                        return "brown"
                    if densities.index(max(densities)) == 5:
                        print("pink")
                        print(densities[5])
                        return "pink"
                    if densities.index(max(densities)) == 6:
                        print("red")
                        print(densities[6])
                        return "red"
                else:
                    print("empty")
                    return "empty"


    return "not_available"

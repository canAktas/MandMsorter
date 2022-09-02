import cv2
import serial
import time
import color
import hsv7Color




arduinoData = serial.Serial("com6", 115200)
time.sleep(2)

width = 640
height = 480
cam=cv2.VideoCapture(0)
#cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
#cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
#cam.set(cv2.CAP_PROP_FPS, 30)
#cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))
time.sleep(0.1)

pyCmd = 0

while True:
    pyCmd = hsv7Color.find_color(cam)
    #pyCmd = input("Enter the color: ")
    pyCmd1 = str(pyCmd)+"\r"
    arduinoData.write(pyCmd1.encode())
    print("message sent ")
    while(arduinoData.inWaiting() == 0):
        time.sleep(0.001)
    print("message received")
    dataPacket = arduinoData.readline()
    dataPacket = str(dataPacket, "utf-8")

import cv2
from cvzone.HandTrackingModule import HandDetector
from time import sleep
import numpy as np
import cvzone
#from pynput.keyboard import Controller
import serial

NULL = 0
ser = serial.Serial(
    port='COM15',
    baudrate=9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
        timeout=0)

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)
detector = HandDetector(maxHands=1, detectionCon=0.8)
finalText = ""
beforeText = ""
phone_number = ""
phone_text = ""
show_number = ""
mode_changer = ""
#keyboard = Controller()
t_flag = 0
CallText_flag = 0
mode_flag = 0
black_image = np.zeros((720, 1080, 3), np.uint8)
checkflag = 0
if mode_flag == 0:
    keys = [["1", "2", "3"],
            ["4", "5", "6"],
            ["7", "8", "9"],
            ["TEXT", "0", "CALL"],
            ["CLE"]]

if mode_flag == 1:
    keys = [["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P"],
            ["A", "S", "D", "F", "G", "H", "J", "K", "L"],
            ["Z", "X", "C", "V", "B", "N", "M"],
            ["SEND"],
            ["CLE"],
            ["BACK"]]

def drawAll(img, buttonList):  #first print
    for button in buttonList:
        x, y = button.pos
        w, h = button.size
        cvzone.cornerRect(img, (button.pos[0], button.pos[1], button.size[0], button.size[1]),
                          20, rt=0)
        cv2.rectangle(img, button.pos, (x + w, y + h), (200, 200, 100), cv2.LINE_4)
        cv2.putText(img, button.text, (x + 5, y + 65),
                    cv2.FONT_HERSHEY_PLAIN, 2, (255, 255, 255), 2)
    return img

class Button():
    def __init__(self, pos, text, size=[85, 85]):
        self.pos = pos
        self.size = size
        self.text = text

buttonList = []
for i in range(len(keys)):
    for j, key in enumerate(keys[i]):
        buttonList.append(Button([(100 * j + 50) + 350, 100 * i + 155], key))

while True:

    if mode_flag == 0:
        keys = [["1", "2", "3"],
                ["4", "5", "6"],
                ["7", "8", "9"],
                ["010", "0", "CLE"],
                ["CALL", "TEXT"]]

        buttonList = []
        for i in range(len(keys)):
            for j, key in enumerate(keys[i]):
                buttonList.append(Button([(100 * j + 50) + 350, 100 * i + 155], key))

    if mode_flag == 1:
        keys = [["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P"],
                ["A", "S", "D", "F", "G", "H", "J", "K", "L"],
                ["Z", "X", "C", "V", "B", "N", "M"],
                ["SEND", " "],
                ["CLE"],
                ["BACK"]]

        buttonList = []
        for i in range(len(keys)):
            for j, key in enumerate(keys[i]):
                buttonList.append(Button([(100 * j + 50), 100 * i + 50], key))




    success, img = cap.read()
    img = cv2.flip(img, 1)
    black_image = np.zeros((720, 1080, 3), np.uint8)
    img = detector.findHands_test(img, black_image)
    lmList, bboxInfo = detector.findPosition(img)
    img = drawAll(img, buttonList)
    if lmList:
        for button in buttonList:
            x, y = button.pos
            w, h = button.size

            if x < lmList[8][0] < x + w and y < lmList[8][1] < y + h: #when it touched
                cv2.rectangle(img, (x - 5, y - 5), (x + w + 5, y + h + 5), (250, 200, 100), cv2.FILLED)
                cv2.putText(img, button.text, (x + 2, y + 65),
                            cv2.FONT_HERSHEY_PLAIN, 2, (255, 255, 255), 2)
                l, _, _ = detector.findDistance(8, 4, img, draw=False)

                #print(l)


                ## when clicked
                if l < 30 and t_flag == 0:
                    #keyboard.press(button.text)
                    cv2.rectangle(img, button.pos, (x + w, y + h), (100, 255, 255), cv2.FILLED)
                    cv2.putText(img, button.text, (x + 3, y + 65),
                                cv2.FONT_HERSHEY_PLAIN, 2, (255, 255, 255), 2)
                    t_flag = 1
                    if button.text == "CLE":
                        finalText = ""
                        button.text = ""
                    elif len(finalText) > 11 and mode_flag == 0:
                        finalText = ""
                        button.text = ""
                    elif button.text == "CALL":
                        phone_number = finalText
                        #ser.write(bytes(phone_number, encoding='ascii'))
                        #CALL PART
                        finalText = ""
                        button.text = ""
                        checkflag = 1
                    elif button.text == "TEXT":
                        phone_number = finalText
                        show_number = phone_number + "/"
                        ser.write(bytes(show_number, encoding='ascii'))
                        print(len(show_number))
                        finalText = ""
                        mode_flag = 1
                        button.text = ""
                        #phone_number = ""
                    elif button.text == "BACK":
                        phone_number = ""
                        finalText = ""
                        mode_flag = 0
                        button.text = ""
                    elif button.text == "SEND":
                        phone_text = finalText
                        #ser.write(bytes(phone_text, encoding='ascii'))
                        #finalText = ""
                        #mode_flag = 0
                        #button.text = ""
                        checkflag = 2
                    else:
                        finalText += button.text

                    sleep(0.05)


                while checkflag == 1:  #check want call

                    keys = ["Y", "N"]

                    buttonList = []
                    for i in range(len(keys)):
                        for j, key in enumerate(keys[i]):
                            buttonList.append(Button([(100 * j + 50) + 400, 100 * i + 300], key))

                    success, img = cap.read()
                    img = cv2.flip(img, 1)
                    black_image = np.zeros((720, 1080, 3), np.uint8)
                    img = detector.findHands_test(img, black_image)
                    lmList, bboxInfo = detector.findPosition(img)
                    img = drawAll(img, buttonList)

                    if lmList:
                        for button in buttonList:
                            x, y = button.pos
                            w, h = button.size

                            if x < lmList[8][0] < x + w and y < lmList[8][1] < y + h:  # when it touched
                                cv2.rectangle(img, (x - 5, y - 5), (x + w + 5, y + h + 5), (250, 200, 100),
                                                cv2.FILLED)
                                cv2.putText(img, button.text, (x + 3, y + 65),
                                                cv2.FONT_HERSHEY_PLAIN, 2, (255, 255, 255), 2)
                                l, _, _ = detector.findDistance(8, 4, img, draw=False)

                                #print(l)

                                if l < 30 and t_flag == 0:
                                    cv2.rectangle(img, button.pos, (x + w, y + h), (100, 255, 255), cv2.FILLED)
                                    cv2.putText(img, button.text, (x + 3, y + 65),
                                                cv2.FONT_HERSHEY_PLAIN, 2, (255, 255, 255), 2)
                                    if button.text == "Y":
                                        phone_number += ","
                                        ser.write(bytes(phone_number, encoding='ascii'))
                                        print(len(phone_number))

                                        #mode_changer = ""
                                        #ser.write(bytes(mode_changer, encoding='ascii'))
                                        #mode_changer = "/"

                                        # CALL PART
                                        finalText = ""
                                        button.text = ""
                                        checkflag = 0
                                        phone_number = ""
                                    elif button.text == "N":
                                        finalText = ""
                                        button.text = ""
                                        checkflag = 0


                                #sleep(0.05)



                                if l > 40:
                                    t_flag = 0

                            cv2.rectangle(img, (200, 50), (1000, 250), (200, 100, 100), cv2.FILLED)  # text bar
                            cv2.putText(img, "Do you want to call?", (305, 100),
                                        cv2.FONT_HERSHEY_PLAIN, 3, (255, 255, 255), 3)
                            cv2.putText(img, phone_number, (305, 200),
                                        cv2.FONT_HERSHEY_PLAIN, 3, (255, 255, 255), 3)
                            cv2.imshow("Image", img)
                            cv2.waitKey(1)

                while checkflag == 2:  #check want text

                    keys = ["Y", "N"]

                    buttonList = []
                    for i in range(len(keys)):
                        for j, key in enumerate(keys[i]):
                            buttonList.append(Button([(100 * j + 50) + 400, 100 * i + 300], key))

                    success, img = cap.read()
                    img = cv2.flip(img, 1)
                    black_image = np.zeros((720, 1080, 3), np.uint8)
                    img = detector.findHands_test(img, black_image)
                    lmList, bboxInfo = detector.findPosition(img)
                    img = drawAll(img, buttonList)

                    if lmList:
                        for button in buttonList:
                            x, y = button.pos
                            w, h = button.size

                            if x < lmList[8][0] < x + w and y < lmList[8][1] < y + h:  # when it touched
                                cv2.rectangle(img, (x - 5, y - 5), (x + w + 5, y + h + 5), (250, 200, 100),
                                                cv2.FILLED)
                                cv2.putText(img, button.text, (x + 3, y + 65),
                                                cv2.FONT_HERSHEY_PLAIN, 2, (255, 255, 255), 2)
                                l, _, _ = detector.findDistance(8, 4, img, draw=False)

                                #print(l)

                                if l < 30 and t_flag == 0:
                                    cv2.rectangle(img, button.pos, (x + w, y + h), (100, 255, 255), cv2.FILLED)
                                    cv2.putText(img, button.text, (x + 3, y + 65),
                                                cv2.FONT_HERSHEY_PLAIN, 2, (255, 255, 255), 2)
                                    if button.text == "Y":
                                        #mode_changer = "T"
                                        #ser.write(bytes(mode_changer, encoding='ascii'))
                                        #mode_changer = ""

                                        phone_text = finalText
                                        phone_text += "."
                                        ser.write(bytes(phone_text, encoding='ascii'))
                                        #mode_changer = "/"
                                        #ser.write(bytes(mode_changer, encoding='ascii'))
                                        #mode_changer = ""

                                        print(len(phone_text))
                                        finalText = ""
                                        mode_flag = 0
                                        button.text = ""
                                        checkflag = 0
                                    elif button.text == "N":
                                        phone_text = ""
                                        finalText = ""
                                        button.text = ""
                                        checkflag = 0

                                #sleep(0.05)

                                if l > 40:
                                    t_flag = 0

                            cv2.rectangle(img, (200, 50), (1000, 250), (200, 100, 100), cv2.FILLED)  # text bar
                            cv2.putText(img, "Do you want to text?", (305, 100),
                                        cv2.FONT_HERSHEY_PLAIN, 3, (255, 255, 255), 3)
                            cv2.putText(img, phone_number, (305, 150),
                                        cv2.FONT_HERSHEY_PLAIN, 3, (255, 255, 255), 3)
                            cv2.putText(img, phone_text, (305, 200),
                                        cv2.FONT_HERSHEY_PLAIN, 3, (255, 255, 255), 3)
                            cv2.imshow("Image", img)
                            cv2.waitKey(1)


                if l > 40:
                    t_flag = 0
    if mode_flag == 0: # call mode
        cv2.rectangle(img, (300, 50), (800, 150), (200, 100, 100), cv2.FILLED)  # text bar
        cv2.putText(img, finalText, (305, 100),
                    cv2.FONT_HERSHEY_PLAIN, 3, (255, 255, 255), 3)
    if mode_flag == 1: # text mode
        cv2.rectangle(img, (250, 350), (1000, 450), (200, 100, 100), cv2.FILLED)  # text bar
        cv2.putText(img, finalText, (280, 430),
                    cv2.FONT_HERSHEY_PLAIN, 3, (255, 255, 255), 3) # text thing
        cv2.putText(img, phone_number, (280, 550),
                    cv2.FONT_HERSHEY_PLAIN, 3, (255, 255, 255), 3) # send number
    #cv2.putText(img, beforeText, (600, 300),
    #            cv2.FONT_HERSHEY_PLAIN, 3, (255, 255, 255), 3)
    cv2.imshow("Image", img)
    cv2.waitKey(1)


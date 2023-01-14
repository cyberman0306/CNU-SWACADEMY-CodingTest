import cv2
from cvzone.HandTrackingModule import HandDetector
from time import sleep
import numpy as np
import cvzone
from pynput.keyboard import Controller

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

detector = HandDetector(detectionCon=0.8)
keys = [["7", "8", "9"],
        ["4", "5", "6"],
        ["1", "2", "3"],
        ["CLE", "0", "CALL"]]

#clear_key = ["DEL"]

finalText = ""

keyboard = Controller()

t_flag = 0
black_image = np.zeros((720, 1080, 3), np.uint8)


def drawAll(img, buttonList):  #first print
    for button in buttonList:
        x, y = button.pos
        w, h = button.size
        cvzone.cornerRect(img, (button.pos[0], button.pos[1], button.size[0], button.size[1]),
                          20, rt=0)
        cv2.rectangle(img, button.pos, (x + w, y + h), (50, 100, 100), cv2.LINE_4)
        cv2.putText(img, button.text, (x + 15, y + 65),
                    cv2.FONT_HERSHEY_PLAIN, 2, (255, 255, 255), 2)
    return img


#
# def drawAll(img, buttonList):
#     imgNew = np.zeros_like(img, np.uint8)
#     for button in buttonList:
#         x, y = button.pos
#         cvzone.cornerRect(imgNew, (button.pos[0], button.pos[1], button.size[0], button.size[1]),
#                           20, rt=0)
#         cv2.rectangle(imgNew, button.pos, (x + button.size[0], y + button.size[1]),
#                       (255, 0, 255), cv2.FILLED)
#         cv2.putText(imgNew, button.text, (x + 40, y + 60),
#                     cv2.FONT_HERSHEY_PLAIN, 2, (255, 255, 255), 3)
#
#     out = img.copy()
#     alpha = 0.5
#     mask = imgNew.astype(bool)
#     print(mask.shape)
#     out[mask] = cv2.addWeighted(img, alpha, imgNew, 1 - alpha, 0)[mask]
#     return out


class Button():
    def __init__(self, pos, text, size=[85, 85]):
        self.pos = pos
        self.size = size
        self.text = text


buttonList = []
for i in range(len(keys)):
    for j, key in enumerate(keys[i]):
        buttonList.append(Button([100 * j + 50, 100 * i + 50], key))

while True:
    success, img = cap.read()
    #success, img = blank_image
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
                cv2.rectangle(img, (x - 5, y - 5), (x + w + 5, y + h + 5), (50, 80, 80), cv2.FILLED)
                cv2.putText(img, button.text, (x + 5, y + 65),
                            cv2.FONT_HERSHEY_PLAIN, 2, (255, 255, 255), 2)
                l, _, _ = detector.findDistance(8, 4, img, draw=False)

                print(l)


                ## when clicked
                if l < 30 and t_flag == 0:  #when it clicked
                    #keyboard.press(button.text)
                    cv2.rectangle(img, button.pos, (x + w, y + h), (0, 255, 0), cv2.FILLED)
                    cv2.putText(img, button.text, (x + 5, y + 65),
                                cv2.FONT_HERSHEY_PLAIN, 2, (255, 255, 255), 2)
                    finalText += button.text
                    t_flag = 1
                    if button.text == "CLE":
                        finalText = ""
                    if len(finalText) > 8:
                        finalText = ""
                    sleep(0.05)



                if l > 40:
                    t_flag = 0




              #  if l == 31:
                    # cv2.rectangle(img, button.pos, (x + w, y + h), (0, 255, 0), cv2.FILLED)
                  #  finalText = ""
               #     sleep(0.15)
                #if a < 20:
                 #   keyboard.press(Key.backspace)
                 #   sleep(0.15)

               # if f < 20:
                #    keyboard.press(Key.space)
                #    sleep(0.15)
    cv2.rectangle(img, (50, 350), (400, 450), (50, 100, 100), cv2.FILLED) #text bar
    cv2.putText(img, finalText, (60, 430),
                cv2.FONT_HERSHEY_PLAIN, 3, (255, 255, 255), 3)

    cv2.imshow("Image", img)
    cv2.waitKey(1)


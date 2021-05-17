import cv2
import numpy as np
from cv2 import morphologyEx

cap = cv2.VideoCapture(0)
back = cv2.imread("/home/achintya/Desktop/code/code for cause/image.jpg")

while cap.isOpened():
    # take each frame
    ret, frame = cap.read()

    if ret:
        # CONVERTING RGN TO HSV
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        # cv2.imshow("hsv", hsv)

        # how to get HSV value;
        # lower HSV value: hue - 10, 100, 100 || higher HSV value: hue+10, 255, 255 || here it is 41

        red = np.uint8([[[0, 0, 255]]])
        hsv_minni = cv2.cvtColor(red, cv2.COLOR_BGR2HSV)
        # gets the HSV value of red from bgr

        #threshold the HSV value to only get colours of red

        l_colour = np.array([0, 100, 100]) # -10, -10, -40
        u_colour = np.array([10, 255, 255]) #+10, +10, +40
        mask = cv2.inRange(hsv, l_colour, u_colour)

        #cv2.imshow("mask", mask) 

        # part1 is all things red
        part1 = cv2.bitwise_and(back, back, mask=mask)
        #cv2.imshow("part1", part1) 

        kernel = np.ones((5,5),np.uint8)
        opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
        closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
        erosion = cv2.erode(mask,kernel,iterations = 1)
        dilation = cv2.dilate(mask,kernel,iterations = 1)

        # we want to ignore red colour and show all the colours       
        
        mask = cv2.bitwise_not(dilation) 
        
        # part2 is all things not red
        part2 = cv2.bitwise_and(frame, frame, mask=mask)

        part3 = part1 + part2

        opening2 = cv2.morphologyEx(part3, cv2.MORPH_OPEN, kernel)
        closing2 = cv2.morphologyEx(part3, cv2.MORPH_CLOSE, kernel)
        erosion2 = cv2.erode(part3,kernel,iterations = 1)
        dilation2 = cv2.dilate(part3,kernel,iterations = 1)

        cv2.imshow("cloak", part3)

        if cv2.waitKey(5) == ord("q"):
            break
cap.release
cv2.destroyAllWindows()



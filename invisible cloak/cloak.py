import cv2

cap = cv2.VideoCapture(0) #THIS IS THE WEBCAM

while cap.isOpened():
    ret, back = cap.read() 
    if ret:
        #back is what camera is recording
        cv2.imshow("image", back)
        if cv2.waitKey(10) == ord("q"):
            #save the image
            cv2.imwrite("image.jpg", back)
            break
    
cap.release()
cv2.destroyAllWindows()
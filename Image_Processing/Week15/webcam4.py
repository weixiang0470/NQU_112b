# pip install opencv-python
import cv2
import numpy as np
# https://stackoverflow.com/questions/61979361/cannot-turn-on-mac-webcam-through-opencv-python
cap = cv2.VideoCapture(1) # Mac m1
# cap = cv2.VideoCapture(0) # Windows
fps = cap.get(cv2.CAP_PROP_FPS)
#print(f'{fps} : fps')

ret , frame = cap.read()
#print(frame.shape)

while(1):
    ret, frame = cap.read()

    frame = cv2.resize(frame,(320,240))
    grayImg = cv2.cvtColor(frame,cv2.COLOR_RGB2GRAY)

    cannyImg = cv2.Canny(grayImg,100,200)

    concat = cv2.hconcat([grayImg,cannyImg])

    cv2.imshow('Canny Img',concat)

    k=cv2.waitKey(1)&0xff
    if k==27 :
        break

cap.release()
cv2.destroyAllWindows()
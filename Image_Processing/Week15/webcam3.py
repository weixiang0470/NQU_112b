# pip install opencv-python
import cv2
import numpy as np
import matplotlib.pyplot as plt
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
    YCrCbImg = cv2.cvtColor(frame,cv2.COLOR_BGR2YCrCb)

    Y,Cr,Cb = cv2.split(YCrCbImg)

    Y2 = cv2.equalizeHist(Y)

    YCrCbImg = cv2.merge([Y2,Cr,Cb])
    ColorImg = cv2.cvtColor(YCrCbImg,cv2.COLOR_YCrCb2BGR)
    concat = cv2.hconcat([frame,ColorImg])

    cv2.imshow('HE image',concat)

    # plt.figure()
    # plt.hist(ColorImg.ravel(),256,[0,256])
    # plt.show()

    k=cv2.waitKey(1)&0xff
    if k==27 :
        break

cap.release()
cv2.destroyAllWindows()
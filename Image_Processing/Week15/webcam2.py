# pip install opencv-python
import cv2

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
    b,g,r = cv2.split(frame)
    #grayImg = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    #thresh,binaryImg = cv2.threshold(grayImg,127,255,cv2.THRESH_BINARY)

    #cv2.imshow('Color Image',frame)
    #cv2.imshow('Gray Image',grayImg)
    #cv2.imshow('Mono Image',binaryImg)

    concat = cv2.hconcat([b,g,r])

    cv2.imshow('concat',concat)

    k=cv2.waitKey(1)&0xff
    if k==27 :
        break

cap.release()
cv2.destroyAllWindows()
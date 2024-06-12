# Haar like face detection

import cv2
cap = cv2.VideoCapture(1) # Mac m1
# cap = cv2.VideoCapture(0) # Windows
fps = cap.get(cv2.CAP_PROP_FPS)
#print(f'{fps} : fps')
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
ret , frame = cap.read()
#print(frame.shape)

while(1):
    ret, frame = cap.read()

    frame = cv2.resize(frame,(320,240))
    grayImg = cv2.cvtColor(frame,cv2.COLOR_RGB2GRAY)

    faces = face_cascade.detectMultiScale(grayImg,scaleFactor=1.3,minNeighbors=2)
    for(x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)

    cv2.imshow('Haar Img',frame)

    k=cv2.waitKey(1)&0xff
    if k==27 :
        break

cap.release()
cv2.destroyAllWindows()
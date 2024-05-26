# pip install opencv-python
import cv2

# https://stackoverflow.com/questions/61979361/cannot-turn-on-mac-webcam-through-opencv-python
cap = cv2.VideoCapture(1) # Mac m1
# cap = cv2.VideoCapture(0) # Windows
fps = cap.get(cv2.CAP_PROP_FPS)
print(f'{fps} : fps')

ret , frame = cap.read()
print(frame.shape)

while(1):
    ret, frame = cap.read()
    cv2.imshow('frame',frame)
    k=cv2.waitKey(30)&0xff
    if k==27 :
        break

cap.release()
cv2.destroyAllWindows()
# **Week 2**
## **Basic DIP**
- Importing needed tools
```
import cv2 
from google.colab.patches import cv2_imshow 
import numpy as np
```
- Read image from path
```
img=cv2.imread("path")
```
- Resize image to 256*256
```
img = cv2.resize(img,(256,256))
```
- Convert image into gray image
```
grayImg=cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
```
- Concat images into horizon arrangement, but only same type of images can do concat
```
ConcatImage=cv2.hconcat([img1,img2,img3]) 
```
- Turn gray image into binary image with more than 50 scale turn into white and others turn into black.
```
thresh,binaryImg=cv2.threshold(grayImg,50,255,cv2.THRESH_BINARY) 
```
- Same function as above code
``` 
monoImg=grayImg
monoImg[monoImg>=50]=255
monoImg[monoImg<50]=0
```
- Show img
```
cv2_imshow(img)
```
- Show img's shape information( Resolutions , Layers), Show layers' information on specific coordinate.
```
print(img.shape)
print(img[0,255])#RGB 分量於點 (0,255)
```
- Split image into R,G,B , but in cv2 it return in B,G,R order
```
b,g,r=cv2.split(img)
```
- Merge images into image
```
mergeImg=cv2.merge([b,g,r]) 
```
- Use numpy to create a img's size "0" array, merge images with R layer with zero array created above, so the result will give red layer of the image
```
zero=np.zeros((img.shape[0],img.shape[1]),dtype="uint8") 
rImg=cv2.merge([zero,zero,r]) 
```

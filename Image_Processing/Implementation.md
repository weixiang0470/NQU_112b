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
- Turn gray image into binary image with more than 50 scale turn into white(255) and others turn into black.
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

# **Week 3**
## Changing brightness of image
```
colorImg=np.float32(img.copy())
colorImg=colorImg-50
colorImg[colorImg<0]=0
colorImg=np.uint8(colorImg)
```
- We can use `cv2.split()` to get R,G,B and minus R of it to reduce red color of the image, then use `cv2.merge()` to get result

## **Negative image**
```
img=255-img
```
## **Gamma correction**
```
def adjust_gamma(image, gamma):
	lookupTable = np.array([((i / 255.0) ** gamma) * 255 
	                        for i in np.arange(0, 256)]).astype("uint8")
	return cv2.LUT(image, lookupTable)
```
- `cv2.LUT` give return of `image` according to `lookupTable`

# **Week 4**
- Sampling （馬賽克）
```
#將圖像解析度縮小
reImg10 = cv2.resize(img.copy(),(32,32), interpolation=cv2.INTER_NEAREST)

#將圖像解析度調大
reImg20 = cv2.resize(reImg10.copy(),(256,256), interpolation=cv2.INTER_NEAREST)
```
- Quantilization 色階調整, 31 階
```
qImg1 = np.float32(img.copy())
qImg1 = (qImg1/255) * 31
qImg1 = np.uint8(qImg1) / 31 * 255
```
- Histogram Processing, 平均化所有顏色分佈(0~255)
```
b,g,r=cv2.split(img.copy())

#平均化顏色分佈
equalizeImg_r=cv2.equalizeHist(r.copy())
equalizeImg_g=cv2.equalizeHist(g.copy())
equalizeImg_b=cv2.equalizeHist(b.copy())

equalize_Img = cv2.merge([equalizeImg_b,equalizeImg_g,equalizeImg_r])

plt.hist(equalize_Img.ravel(),256,[0,256]) #畫出顏色分佈
plt.show()
```

# **Week 5**
- Smooth Filter/Blur Filter
```
kernel = np.array([[1,1,1],[1,1,1],[1,1,1]])/9
smoothImg=cv2.filter2D(src=img.copy(),ddepth=-1,kernel=kernel) #Add value of 9 pixels and divide by 9, then put it back to middle pixel

blurImg=cv2.blur(img.copy(),(3,3)) #Use 3*3 mask to do blur
```
- Subtraction
```
Gray_Image = cv2.cvtColor(Colour_Image,cv2.COLOR_RGB2GRAY)

Subtract_Image = cv2.absdiff(Gray_Image1,Gray_Image2)
```
- Create mask image
```
ret,Mask_Image=cv2.threshold(Subtract_Image,40,255,cv2.THRESH_BINARY)
```
- AND with mask image
```
Result_Image = cv2.bitwise_and(Colour_Image,Colour_Image,mask=Mask_Image)
```
- Reverse image
```
Mask_Image = cv2.bitwise_not(Mask_Image)
```
- Combined images
```
Final_Image = Result_Image1 + Result_Image2
```
# **Week 6**
- Smooth filter 
```
kernel=np.array([
	[1,1,1],
	[1,1,1],
	[1,1,1]
])/9

Smooth_Img=cv2.filter2D(src=Origin_img,ddepth=-1,kernel=kernel)
```
- Smooth filter with cv2.blur
```
Smooth_img1 = cv2.blur(Origin_img,(5,5))
Smooth_img2 = cv2.blur(Origin_img,(7,7))
```
- Gaussian blur
```
Gaussian_blur_img1 = cv2.GaussianBlur(Origin_img,(5,5),0)
Gaussian_blur_img2 = cv2.GaussianBlur(Origin_img,(7,7),0)
```
- Smooth filter with veriant type
```
kernel=np.array([
	[1,2,1],
	[2,4,2],
	[1,2,1]
])/16

Smooth_Img=cv2.filter2D(src=Origin_img,ddepth=-1,kernel=kernel)
```
- Median blur, can clean small dot on image(胡椒鹽), create water color painting effect 
```
Median_img = cv2.medianBlur(Origin_img,3)
Median_img = cv2.medianBlur(Origin_img,5)
```
- Laplacian filter, for sharpen image
```
kernel=np.array([
	[0,1,0],
	[1,-4,1],
	[0,1,0]
])

kernel=np.array([
	[0,-1,0],
	[-1,4,-1],
	[0,-1,0]
])

kernel=np.array([
	[0,-1,0],
	[-1,5,-1],
	[0,-1,0]
])

kernel=np.array([
	[1,1,1],
	[1,-8,1],
	[1,1,1]
])

kernel=np.array([
	[-1,-1,-1],
	[-1,8,-1],
	[-1,-1,-1]
])

kernel=np.array([
	[-1,-1,-1],
	[-1,9,-1],
	[-1,-1,-1]
])
Laplacian_img = cv2.filter2D(src=Origin_img,ddepth=-1,kernel=kernel)
```
- Unsharping image
```
Gaussian_img = cv2.GaussianBlur(Origin_img,(5,5),0)
Unsharping_img = cv2.addWeighted(Origin_img,2.0,Gaussian_img,-1.0,0)
```
- High boost image
```
kernel=np.array([
	[-1,-1,-1],
	[-1,9.5,-1],
	[-1,-1,-1]
])

Highboost_img=cv2.filter2D(src=Origin_img,ddepth=-1,kernel=kernel)
```
- First derivatives(the gradient),sobel_x and sobel_y, on gray image to find horizon and vertical side
```
kernel_x = np.array([
	[-1,-2,-1],
	[0,0,0],
	[1,2,1]
])

kernel_y = np.array([
	[-1,0,1],
	[-2,0,2],
	[-1,0,1]
])

Sobel_x_img = cv2.filter2D(src=Origin_img,ddepth=-1,kernel=kernel_x)
Sobel_y_img = cv2.filter2D(src=Origin_img,ddepth=-1,kernel=kernel_y)

Sobel_img = cv2.addWeighted(Sobel_x_img,1,Sobel_y_img,1,0)
```
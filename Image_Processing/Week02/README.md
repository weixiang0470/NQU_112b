# **DIP**
- Digital Image Processing
- Digital images
    - pixel : location(coordinate) + value(RGB)
- Frequency 
    - Gamma-Ray Imaging : $3×10^{19} Hz ++$
    - X-ray Imaging : $3×10^{16} \to 3×10^{19} Hz$
    - Visible : $430x10^{12} \to 750x10^{12} Hz$
    - Infrared : $300x10^{9} \to 430x10^{12} Hz$
    - MRI : $1x10^{6} \to 300x10^{6} Hz$

## **Simple Image Formation Model**
- Binary Image(Mono) : Only black or white, 0=black, 1=white
- Gray Image(Gray-scale) : Having black scale (0~255), 0=black, 255=white
- Color image : Image with colours, RGB
- 8 bits to represent cause 8 bits = 1 bytes, and also 8 bits is enough to represent the colours-scale

## **加法混色**
1. 同時加法混色 ： 電影院
2. 繼時加法混色
3. 並置加法混色 ： 一個pixel包含3個分量（RGB）


## **副檔名**
- GIF ： 動畫
- JPG ： 壓縮
- PNG ： 加上透明(alpha)
- BMP ： 不失真

# **OpenCV**
- Open Source Computer Vision Library
- Image Processing, Computer Vision, Pattern Recognition
- 1999, Intel started
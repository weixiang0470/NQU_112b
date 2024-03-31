# **手寫辨識**
- Keras MNIST
- numpy ： 處理數值分析
- 二維轉成一維向量（數字影像的數字標準化）,60000張圖像,784(28*28)個column的array/圖像
```
x_train = x_train_image.reshape(60000,784).astype('float32')
```
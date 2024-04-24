# **CNN**
- CNN v.s MLP : CNN多了卷積層、池化層
- 卷積層 : 產生更多影像, 8 images -> 64 images, resolution stay the same
    - use different **filter weight** to create multiple images, to have different features
- 池化層 : 將影像縮小，ex，8x8 -> 4x4
    - Max-Pool : For image downsampling, get the max number in an area,ex,
```
[[2,6,2,7],
 [1,8,4,2],
 [7,1,3,9],
 [1,7,2,4]]

[[8,7],
 [7,9]]
```
- 平坦層 : Turn images into 1 dimension,ex, 36 images with 7x7 resolutions will turn into 1764 float numbers as neuron input.


# **CIFAR-10**
- Images datasets including airplane,automobile,cat,bird,...
- RGB images
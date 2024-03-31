# **Local Enhancement**
- 取一小區塊來做HE，依序將整張圖像做完

## **算術與邏輯運算**
- AND
    - 黑色保留（取最小）
- OR
    - 白色保留（取最大）
- Image Subtraction
    - 看兩張圖像的差異

## **Space Filter**
- 平滑濾波器
    - 模糊化
    - 將周圍的pixel值加總在除以pixel數然後放回中心點，例：Mask=9，將9宮格的pixel值加總在除以9並放回中心。
    
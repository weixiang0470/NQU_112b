# **取樣與量化**
- 取樣 ： 越高->圖形的“形狀”越接近
- 量化 ： 越高->圖形的“顏色”越接近
# **摩爾紋**
- 是一種在數位照相機或者掃描器等裝置上，感光元件出現的高頻干擾的條紋，是一種會使圖片出現彩色的高頻率不規則的條紋。摩爾紋因為是不規則的，所以並沒有明顯的形狀規律。

# **距離測量**
- (x,y) 與 (s,t)
- 歐幾里德
    - $D_{e} = \sqrt{(x-s)^2 + (y-t)^2}$
- 市街距離
    - $D_{4}  = |x-s| + |y-t|$
- 棋盤距離
    - $D_{8}  = max(|x-s| , |y-t|)$

# **灰階**
- （R+G+B）/3 ： 相加時可能超過255就會產生溢位（1 byte = 0～255）
- R/3 + G/3 + B/3
- RGB 為同值時為灰階，ex：（100，100，100）與（200，200，200）都是灰階影像只是較暗與較亮

# **Image Enhancement**
- Enhancement : To **improve** the usefulness of the image by some transformation function(s)
1. Image Negative
    - Range[0,L-1]
    - T(r) = L-1-r
2. Brightness
    - Gamma Correction(Power-Law Transformation)
    - Log transformation
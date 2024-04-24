# **大小圖轉換**
- 大 -> 小 ： 取平均值放進去
- 小 -> 大 ： 最近鄰居、線性
    - 線性 ： 上一格是 4， 那就補 5
    - 最近鄰居 ： 看最近一格是多少就用多少

# **Histogram Processing**
- High-contrast is better than low-contrast
$$h(v)=round({{cdf(v) - cdf_{min}}\over{(M * N)-cdf_{min}}}* (L-1))$$
- `M * N` : resolution
- `L - 1` : Maximum brightness(255)
- `cdf(v)` : accumulate of the brightness's number, ex: $52 have 2, 53 have 1, cdf(52) = 2 , cdf(53)=3$

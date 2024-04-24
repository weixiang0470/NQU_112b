# **偏微分**
- $f(x,y) = x^2 + xy + y^2$
- 針對 x 的偏微分為
    - ${{\delta f}\over{\delta x}} = {2x + y}$
- 針對 y 的偏微分為
    - ${{\delta f} \over {\delta y}} = {x + 2y}$

# **梯度**

- 梯度(grad)為各個變數的偏微分的所形成的向量
    - $f(x,y) = x^2 + xy + y^2$
    - $grad = [ 2x+y , x+2y ]$
    - EX : 函數 f 在 點 (1，2) 的梯度
        - grad(f) = [4,5]

# **Entropy & CrossEntropy**
- Entropy
$$H(X) =  - \sum_{x\in X} p(x) *log * p(x)$$
- CrossEntropy
$$H(p,q) =  - \sum_{x\in X} p(x) *log *q(x)$$

# **學習資源**
- [PyTorch](https://pytorch.org)
- [Dive into Deep Learning](https://d2l.ai)
- [Hung-yi Lee](http://speech.ee.ntu.edu.tw/~hylee/index.php)
# **現代AI套件**
1. pytorch（動態微分）
    - `pip3 install torch torchvision`
    - `import torch`
2. tensorflow（靜態微分）
    - `import tensorflow`

動態微分
- 可以在中間去修改模型

靜態微分
- 必須等模型訓練好才能修改

# **Entropy**
$$\sum_i{P(x)*log(p(x))}$$
## 機率場
- Coin : $1\over2$(正)，$1\over2$(反), 可用 1,0 來表示
## **Cross Entropy**
$$\sum_i{P(x)*log(q(x))}$$
- If $q_i \to p_i$ will get best result
- $p(x)$ is the true possibility, $q(x)$ is the possibility we guessed

# **softmax**
$${{e^{n_i}} \over {\sum_i{e^{n_i}}}}$$
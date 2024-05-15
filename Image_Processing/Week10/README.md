# **Transform Matrix**
- Use a transform matrix A to make changes to it
```
|x'|     |x|
|y'| = A*|y|
|1 |     |1|
```
- `x'` : new x
- `y'` : new y
- `A`  : Transform Matrix A
- Let 
    - $x' = x*a_{11} + y*a_{12}+a_{13}$
    - $y' = x*a_{21} + y*a_{22}+a_{23}$
- Scalling/Reflection matrix A
    - $x' = C_x * x$
    - $y' = C_y * y$
```
|Cx 0  0|
|0  Cy 0|
|0  0  1|
```
- Rotation
    - $x' = x*cosB-y*sinB$
    - $y' = x*sinB+y*cosB$
```
|cosB -sinB 0|
|sinB  cosB 0|
| 0     0   1| 
```
- Translation
    - $x' = x * T_x$
    - $y' = y * T_y$
```
|1  0  Tx|
|0  1  Ty|
|0  0  1 |
```


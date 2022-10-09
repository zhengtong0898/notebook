
# 二元一次方程组  
**二元:** 两个未知数, 通常是 x 和 y.  
**一次:** 未知数不带平方.  


&nbsp;  
### 判断是否有解  
> **有唯一解:** $ {a_1 \over a_2} \ne {b_1 \over b_2}  $  


> **无解:** $ {a_1 \over a_2} = {b_1 \over b_2} \ne {c_1 \over c_2} $  


> **有无穷多的解:** $ {a_1 \over a_2} = {b_1 \over b_2} = {c_1 \over c_2} $  


&nbsp;  
### 解方程  

> 代入消元法  

- **例-1**  
$$ 
\begin{align}
    gcd(x, y) =
    \begin{cases}
        x                    & y = 0 \\
        gcd(y, x \ mod \  y) & y > 0
    \end{cases}
\end{align}
$$


> 加减消元法  



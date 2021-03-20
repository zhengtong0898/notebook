`O(n^2)`时间复杂度也被称为平方阶复杂度, 
双层循环， 任意一层的变量增大, 循环次数都会按平方量级增加.   

```python
def main(n, k):
    count = 1
    for i in range(n):              # n * k 次循环 ~=(接近) n^2, 所以按 n^2 来评估.
        for j in range(k):
            count += 1
```

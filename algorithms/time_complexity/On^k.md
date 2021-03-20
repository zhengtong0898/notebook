`O(n^k)`时间复杂度也被称为k次方阶复杂度, 
k层循环， 任意一层的变量增大, 循环次数都会按k立方量级增加.   

下面的代码的复杂度是 `O(n^5)`, 即: 5次方阶复杂度.
```python
def main(v, w, x, y, z):
    count = 1
    
    for g in range(v):
        for h in range(w):
            for i in range(x):
                for j in range(y):
                    for k in range(z):
                        count += 1

    print(count)
```
`O(n^3)`时间复杂度也被称为立方阶复杂度, 
三层循环， 任意一层的变量增大, 循环次数都会按立方量级增加.   

```python
def main(x, y, z):
    count = 1

    for i in range(x):
        for j in range(y):
            for k in range(z):
                count += 1

    print(count)
```
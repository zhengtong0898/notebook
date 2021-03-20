`O(nlogn)`被称为线性对数复杂度, 
遍历 n 个次, 每次遍历采用对半跳跃或对数跳跃处理, 
这两种情况叠加在一起被称为线性对数复杂度, 例如:
```python
result = []
data1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
data2 = [10, 1, 11, 2, 20, 3, 31, 4, 50, 5, 100, 6, 500, 7, 32, 8, 9]
for value in data1:
    item = binary_search(data2, value)
    result.append(item)
```

&nbsp;  
### 参考
[Understanding time complexity with Python examples](https://towardsdatascience.com/understanding-time-complexity-with-python-examples-2bda6e8158a7)

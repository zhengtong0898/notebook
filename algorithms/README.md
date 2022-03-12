
### 常见的时间复杂度

| 符号 | 英文名 | 中文名 |
|---|:---:|:---:|
| O(1) | Constant Time  | [常量阶](time_complexity/O1.md) |
| O(logn) | Logarithmic Time | [对数阶](time_complexity/Ologn.md) |
| O(n) | Linear Time | [线性阶](time_complexity/On.md) |
| O(nlogn) | Quasilinear Time | [线性对数阶](time_complexity/Onlogn.md) |
| O(n^2) | Quadratic Time | [平方阶](time_complexity/On^2.md) |
| O(n^3) | Cubic Time | [立方阶](time_complexity/On^3.md) |
| O(2^n) | Exponential Time | [指数阶](time_complexity/O2^n.md) |
| O(n!) |Factorial Time | [阶乘阶](time_complexity/On!.md) |


&nbsp;  
**log的底数是多少?**    
在数学中: log的底数是10.  
在算法中: log的底数是2, 因为算法中最佳效果是二分, 所以底数是2.
```python3
import math

math.log2(2)  == 1 
math.log2(4)  == 2  
math.log2(8)  == 3  
...
math.log2(1073741824) == 30     # 10亿个元素, 只需要30次比较就能精准命中.      
```

![Big-O-Complexity-Chart](./Big-O-Complexity-Chart.jpg)   



&nbsp;  
&nbsp;  
### 排序  

|稳定性|算法名(中)|算法(英)|最好复杂度|均摊复杂度|最差复杂度|程度|
|---|---|---|---|---|---|---|
|稳定|-|tim sort|O(n)|O(n log n)|O(n log n)|Medium|
|稳定|[冒泡排序](./sorts/ComparisonSorting/bubble_sort.py)|bubble sort|O(n)|O(n^2)|O(n^2)|Easy|
|稳定|[插入排序](./sorts/ComparisonSorting/insertion_sort.py)|insertion sort|O(n)|O(n^2)|O(n^2)|Easy|
|稳定|[归并排序](./sorts/ComparisonSorting/merge_sort.py)|merge sort|O(n log n)|O(n log n)|O(n^2)|Medium|
|稳定|[桶排序](./sorts/bucket_sort.py)|bucket sort|O(n + k)|O(n + k)|O(n^2)|Easy|
|稳定|[基数排序](./sorts/radix_sort.py)|radix sort|O(n + k)|O(n + k)|O(n + k)|Medium|
|稳定|[计数排序-复杂版本](./sorts/count_sort_complex.py)|count sort|O(n + k)|O(n + k)|O(n + k)|Medium|
|不稳定|[计数排序-简单版本](./sorts/count_sort_simple.py)|count sort|O(n + k)|O(n + k)|O(n + k)|Easy|
|不稳定|[选择排序](./sorts/ComparisonSorting/selection_sort.py)|selection sort|O(n^2)|O(n^2)|O(n^2)|Easy|
|不稳定|[希尔排序](./sorts/ComparisonSorting/shell_sort.py)|shell sort|O(n log n)|O(n log n)|O(n^2)|Easy|
|不稳定|[快速排序-递归版本](./sorts/ComparisonSorting/quick_sort_recursion.py)|quick sort|O(n log n)|O(n log n)|O(n^2)|Medium|
|不稳定|[快速排序-分割版本](./sorts/ComparisonSorting/quick_sort_partition.py)|quick sort|O(n log n)|O(n log n)|O(n^2)|Medium|
|不稳定|[堆排序](./sorts/heap_sort.py)|heap sort|O(n log n)|O(n log n)|O(n log n)|Medium||

> #### 稳定性  
> 排序前后两个相等的数相对位置不变, 则算法稳定, [参考资料](https://www.baeldung.com/cs/stable-sorting-algorithms).   
> ![stable-vs-unstable](https://www.baeldung.com/wp-content/uploads/2019/08/Stable-vs-Unstable-1.png)  



&nbsp;  
&nbsp;
### 搜索


&nbsp;  
&nbsp;  
### 数据结构  



&nbsp;  
&nbsp;   
### 学习资源
[C语言中文网](http://c.biancheng.net/data_structure/)   
[数据结构、算法与应用](https://book.douban.com/subject/26421141/)   
[极客时间-王争-数据结构与算法之美](https://time.geekbang.org/column/126)   
[LeetCode101题精讲](./LeetCode101-A-LeetCode-Grinding-Guide-(CPP-Version).pdf)   
[Understanding time complexity with Python examples](https://towardsdatascience.com/understanding-time-complexity-with-python-examples-2bda6e8158a7)  
[usfca algorithms](https://www.cs.usfca.edu/~galles/visualization/Algorithms.html)  
[visualgo](https://visualgo.net/en)  

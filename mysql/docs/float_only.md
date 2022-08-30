
### 浮点类型

目前浮点遵循 [IEEE 754-1985](https://en.wikipedia.org/wiki/IEEE_754-1985) 标准来存储和展示,    
存储方面: 它采用32-bit(4个byte: 4个8-bit段)来存储, 存储结构: sign(1-bit) / exponent(8-bit) / mantissa(23-bit) ; 
1. 将浮点类型的值转换位二进制, [具体算法](./float_only.py#L11)   

展示方面: 通过特定算法来将二进制转换成十进制来显示, 算法主要分为三个部分.  
1. 将二进制转换为浮点二进制: 也就是说找到 '.' 并算出它的位置, 这个 '.' 起到分割整数和浮点的作用, [具体算法](./float_only.py#L32) .  
   > **sign** 这个段用来表示: 0为正数(+), 1为负数(-).  
   > **exponent** 这个段用来计算 '.' 的偏移量.  
   > **mantissa** 这个段有 23-bit, 用 2**23 得到 8388608 , 这表示精度最大宽度是7个位(含整数、浮点数)， 当超过精度最大范围时采取四舍五入.  
2. 通过浮点二进制计算出 '.' 左侧的整数部分, [具体算法](./float_only.py#L55)  
3. 通过浮点二进制计算出 '.' 右侧的浮点部分. [具体算法](./float_only.py#L66) 




### 参考  

https://dev.mysql.com/doc/refman/8.0/en/floating-point-types.html

https://www.h-schmidt.net/FloatConverter/IEEE754.html

https://zhuanlan.zhihu.com/p/137616403

https://blog.51cto.com/xiagao/3219027

https://en.wikipedia.org/wiki/Single-precision_floating-point_format#Exponent_encoding

https://stackoverflow.com/questions/44339668/mysql-float-type-range-and-precision-confusion

https://github.com/ajdawson/fconvert/blob/master/fconvert/__init__.py

https://www.bilibili.com/video/BV1tK411P7nh

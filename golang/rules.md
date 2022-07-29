
- `_`下划线变量  
当变量赋值给下划线`_`变量时, 编译器会丢弃该值; 引用下划线变量会报错.  


- 变量定义但未使用  
变量定义但未使用, 会报错.   


- public  
1). 大写字母开头的变量.  
2). 大写字母开头的函数.  


- private  
1). 小写字母开头的变量.  
2). 小写字母开头的函数.  


- array  
定长数组


- slice  
动态数组


- Variadic functions(变参)  
```go
package main

import "fmt"

func myfunc(args ...int) {

	for index, arg := range args {
		fmt.Print(index, arg, "\n")
	}

}

func main() {
	items := []int{10, 20, 30, 40, 50}
	myfunc(items...)
}


# 输出
0 10
1 20
2 30
3 40
4 50
```


- 指针   
一个指针占位是8bytes.


- 函数的形参和实参     
对于基础类型, golang的函数默认采取完全拷贝策略.    
如果想要避免完全拷贝, 需要在定义和传递两端做一些特殊声明.    
在定义端使用 `*type` 来接参数.    
在定义端使用 `*variable` 来操作指针背后的实际值.  
在传值端使用 `&variable` 来传递参数.    





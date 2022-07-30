
### `_`下划线变量  
当变量赋值给下划线`_`变量时, 编译器会丢弃该值; 引用下划线变量会报错.  


&nbsp;  
### 变量定义但未使用  
变量定义但未使用, 会报错.   


&nbsp;  
### public  
1). 大写字母开头的变量.  
2). 大写字母开头的函数.  


&nbsp;  
### private  
1). 小写字母开头的变量.  
2). 小写字母开头的函数.  


&nbsp;  
### array  
定长数组


&nbsp;  
### slice  
动态数组


&nbsp;  
### Variadic functions(变参)  
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
# 0 10
# 1 20
# 2 30
# 3 40
# 4 50
```


&nbsp;  
### 指针   
一个指针占位是8bytes.


&nbsp;  
### 函数的形参和实参     
对于基础类型, golang的函数默认采取完全拷贝策略.    
如果想要避免完全拷贝, 需要在定义和传递两端做一些特殊声明.    
在定义端使用 `*type` 来接参数.    
在定义端使用 `*variable` 来操作指针背后的实际值.  
在传值端使用 `&variable` 来传递参数.    



&nbsp;  
### defer  
两种情况会触发执行defer指令:  
1). 当函数执行结束后, 会执行defer函数;  
2). 当函数执行遇到panic后, 会执行defer函数;   
因此可以理解为defer关键字是一个teardown的行为.  
当函数体内有多个defer指令时, 采取LIFO策略执行这些defer指令.  
```go
package main
import "fmt"


func example(text string) {
    fmt.Println(text)
}


func main() {
    defer example("11111")
    defer example("22222")
    defer example("33333")
    fmt.Println("hello world!")
}

# 输出
# hello world!
# 33333
# 22222
# 11111
```


&nbsp;  
### recover  
当执行recover()时, 发现没有panic则返回nil.  
当执行recover()时, 发现有panic则返回panic对象.  
recover只能定义在defer指定的函数内.  
recover的覆盖场景其实就是另一种形态的try,  
当发现recover返回的是panic对象时可以做一些判断,   
如果符合预期则继续业务处理,   
如果不符合预期则可以让panic继续下去终止程序.  
```go
package main
import "fmt"

func panicHandler(){
    rec := recover()
    if rec != nil {
        fmt.Println("RECOVER", rec)
    } else {
        fmt.Println("sssss")
    }
}


func employee(name *string, age int){
    defer panicHandler()
    if age > 75 {
        panic("Age cannot be greater than retirement age")
    }
}


func main() {
    empName := "Samia"
    age := 95

    employee(&empName, age)
}

# 输出
# RECOVER Age cannot be greater than retirement age
```


&nbsp;  
### main和init
`package main`是程序入口文件, `func main() {}`是程序入口函数, `func init() {}`是当前程序的前置`hook`.      
`package pkg`是程序包, `func init() {}`是当前包的前置`hook`.  
```shell
[root@localhost ~]# tree recov/
recov/
├── go.mod
├── gun
│   └── se.go
└── main.go

1 directory, 3 files


[root@localhost ~]# cd recov/ 
[root@localhost ~]# cat go.mod 
module recov

go 1.18


[root@localhost ~]# cat main.go 
package main
import "fmt"
import _ "recov/gun"


func init() {
    fmt.Println("package main: init")
}


func main() {
    fmt.Println("package main: hello world!")
}


[root@localhost ~]# cat gun/se.go 
package gun
import "fmt"


func init() {
    fmt.Println("package gun: init")
}


# 输出
# 先执行package gun的init前置函数
# 再执行package main的init前置函数
# 最后执行package main的main入口函数
[root@localhost ~]# go run main.go 
package gun: init
package main: init
package main: hello world!

```
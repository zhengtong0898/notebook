
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
[root@localhost recov]# cat go.mod 
module recov

go 1.18


[root@localhost recov]# cat main.go 
package main
import "fmt"
import _ "recov/gun"


func init() {
    fmt.Println("package main: init")
}


func main() {
    fmt.Println("package main: hello world!")
}


[root@localhost recov]# cat gun/se.go 
package gun
import "fmt"


func init() {
    fmt.Println("package gun: init")
}


# 输出
# 先执行package gun的init前置函数
# 再执行package main的init前置函数
# 最后执行package main的main入口函数
[root@localhost recov]# go run main.go 
package gun: init
package main: init
package main: hello world!

```

&nbsp;  
### goto  
用goto来实现一个`while`循环
```shell
[root@localhost ~]# mkdir gotoprac


[root@localhost ~]# cd gotoprac
[root@localhost ~]# go mod init gotoprac


[root@localhost gotoprac]# cat main.go 
package main
import "fmt"


func main() {

    i := 0

Here:

    if i < 10 {
        fmt.Println(i)
	i++
	goto Here
    }

}


# 输出
[root@localhost gotoprac]# go run main.go
0
1
2
3
4
5
6
7
8
9
```

&nbsp;  
### goroutine
goroutine是一个执行线程, 它从线程池中获取一个执行线程来执行一个函数.  

`runtime.GOMAXPROCS`负责管理线程池的大小,   
在go1.5版本之前, 它的默认值是1,   
在go1.5版本之后, 它的默认值是cpu个数, 例如: I7 8770 是6核12线程, 所以值为12.  

当线程池的值为1时, 表示只有一个线程在运行多个goroutine, go的表现是模拟cpu做时间  
切片去运行多个的goroutine, 每个goroutine运行一小撮时间(比如说: 20us).

Example-1: 当线程池大小为1时, 同时开启多个goroutine, 仅占用一个cpu.
```shell
[root@localhost ~]# mkdir goroutinee
[root@localhost ~]# cd goroutinee
[root@localhost goroutinee]# go mod init goroutinee
[root@localhost goroutinee]# go get golang.org/x/sys/unix
[root@localhost goroutinee]# go mod tidy
[root@localhost goroutinee]# cat main.go 
package main


// refer
// https://blog.actorsfit.com/a?ID=00750-92325ec1-fe3f-4670-aadb-b68f8510f3d5
// https://blog.csdn.net/liangzhiyang/article/details/52669851?utm_source=blogxgwz3
// https://draveness.me/golang/docs/part3-runtime/ch06-concurrency/golang-goroutine/
// https://golang.design/go-questions/sched/goroutine-vs-thread/
// https://morsmachine.dk/go-scheduler
import (
    "bytes"
    "fmt"
    "runtime"
    "strconv"

    "golang.org/x/sys/unix"
)


func getGoID() uint64 {
    b := make([]byte, 64)
    b = b[:runtime.Stack(b, false)]
    b = bytes.TrimPrefix(b, []byte("goroutine "))
    b = b[:bytes.IndexByte(b, ' ')]
    n, _ := strconv.ParseUint(string(b), 10, 64)
    return n
}


func say(text string) {
    for i := 1; i > 0; i++ {
        _ = fmt.Sprintf("[process-id: %d; thread-id: %d; goroutine-id:%d] %s: %d\n", unix.Getpid(), unix.Gettid(), getGoID(), text, i)
    }
}


func main() {
    runtime.GOMAXPROCS(1)
    go say("world 1")
    go say("world 2")
    go say("world 3")
    go say("world 4")
    say("hello")
}


[root@localhost goroutinee]# go mod tidy
[root@localhost goroutinee]# go run main.go

# 开另外一个窗口来观察, %CPU字段占用一颗cpu的100%
[root@localhost goroutinee]# top -c
    PID USER      PR  NI    VIRT    RES    SHR S  %CPU  %MEM     TIME+ COMMAND  
  75124 zt        20   0  703420   6580   1132 S 100.3   0.0   0:36.18 /tmp/go-build3384966463/b001/exe/main                                                                                                                                                                              

```

Example-2: 当线程池大小为12时, 开启多少个goroutine就会吃满多少个cpu.  
```shell

// 代码与上面一致.
func main() {
    // runtime.GOMAXPROCS(1)         // 注释掉线程池设置, 让它使用默认值: 12(cpu个数).
    go say("world 1")
    go say("world 2")
    go say("world 3")
    go say("world 4")
    say("hello")
}

[root@localhost goroutinee]# go run main.go

# 开另外一个窗口来观察, %CPU字段占用一颗cpu的500%
[root@localhost goroutinee]# top -c
    PID USER      PR  NI    VIRT    RES    SHR S  %CPU  %MEM     TIME+ COMMAND  
  75124 zt        20   0  703420   6580   1132 S 500.3   0.0   0:36.18 /tmp/go-build3384966463/b001/exe/main   
```

Example-3: 当线程池大小为1时, 一个goroutine堵塞, 不影响另外一个goroutine.  
也就是说我可以放心的去写堵塞代码, goroutine会帮我挂起堵塞代码，帮我唤醒, 同时不会堵塞其他goroutine.  
```shell
[root@localhost goroutinee]# cat main.go 
package main

// refer
// https://blog.actorsfit.com/a?ID=00750-92325ec1-fe3f-4670-aadb-b68f8510f3d5
// https://blog.csdn.net/liangzhiyang/article/details/52669851?utm_source=blogxgwz3
// https://draveness.me/golang/docs/part3-runtime/ch06-concurrency/golang-goroutine/
// https://golang.design/go-questions/sched/goroutine-vs-thread/
// https://morsmachine.dk/go-scheduler
import (
	"bytes"
	"fmt"
	"runtime"
	"strconv"
	"time"

	"golang.org/x/sys/unix"
)


const (
    date_format = "2006-01-02 15:04:05.000000"
)


func getGoID() uint64 {
    b := make([]byte, 64)
    b = b[:runtime.Stack(b, false)]
    b = bytes.TrimPrefix(b, []byte("goroutine "))
    b = b[:bytes.IndexByte(b, ' ')]
    n, _ := strconv.ParseUint(string(b), 10, 64)
    return n
}


func say_block(text string) {
    fmt.Printf("[%s: process-id: %d; thread-id: %d; goroutine-id:%d] %s\n", time.Now().Format(date_format), unix.Getpid(), unix.Gettid(), getGoID(), text)
    time.Sleep(10 * time.Second)
    fmt.Printf("[%s: process-id: %d; thread-id: %d; goroutine-id:%d] %s\n", time.Now().Format(date_format), unix.Getpid(), unix.Gettid(), getGoID(), text)
}


func say(text string) {
    j := 1
    for i := 1; i > 0; i++ {
        if i > 100000000 {
            fmt.Printf("[%s: process-id: %d; thread-id: %d; goroutine-id:%d] %s: %d\n", time.Now().Format(date_format), unix.Getpid(), unix.Gettid(), getGoID(), text, j)
            i = 1
            j += 1
        }
    }
}


func main() {
    runtime.GOMAXPROCS(1)
    go say_block("world block")
    go say("world 2")
    say("hello")
}

[root@localhost goroutinee]# go run main.go

# 三个goroutine都在同时运行, 堵塞的goroutine-1并没有堵塞其他两个goroutine.
# goroutine-1: world block
# goroutine-2: world 2
# goroutine-3: hello 
```

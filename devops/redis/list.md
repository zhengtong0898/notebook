### 栈(LIFO)  
lpush   
lpop  


### 队列(FIFO)  
lpush  
rpop   


### 堵塞队列(blocking)  
当队列有值时, 与 lpop 和 rpop 一样.  
当队列没有值时, 它会帮你堵塞住直到有值, 简化你的代码(不需要你自己写循环了).  
blpop  
brpop  


### 列表扫描(LIFO)
lrange key 0 -1


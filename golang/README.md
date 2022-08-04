# 学习资料  
https://github.com/astaxie/build-web-application-with-golang/blob/master/zh/SUMMARY.md

# interface
1. Go通过interface实现了duck-typing
2. 从变量赋值角度看: interface可以存储任何类型的值
3. 从函数参数角度看: 函数声明了interface类型后, 可以接受任何类型的实参
4. 嵌套interface, 父interface会拥有子interface的方法
5. 度量interface的值的类型: ([类型转换](https://stackoverflow.com/questions/49448302/convert-interface-to-struct)) value.(int) / value.(string)
6. 度量interface的值的类型: ([反射](https://golangbot.com/reflection/)) reflect.TypeOf; 获得该变量的实际类型.

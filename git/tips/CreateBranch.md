### 如何创建一个分支?
创建分支指的是，在当前分支的基础上，克隆一份代码出来放在另外一个分支中。  
也就是说新创建出来的分支，与当前分支的代码文件以及commit是一致的。  

&nbsp;  
### 查看当前分支
```shell
$ git branch --list
* master
```

&nbsp;  
### 创建一个分支
```shell
$ git checkout -b my-new-branch
```

&nbsp;  
> 关键信息   
> checkout: 当跟随的分支名参数存在时, 切换到该分支.  
> checkout: 当跟随的分支名参数不存在时, 创建一个分支.  
> 
> -b: 创建分支，并切换到该分支.   

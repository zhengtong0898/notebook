### 如何重命名一个分支?
```shell
# 查看分支清单, 当前所在的分支是: my-branch
$ git branch --list
  master
* my-branch

# 将 my-branch 重命名为 my-new-branch 
$ git branch -m my-new-branch

# 再次查看分支清单
$ git branch --list
  master
* my-new-branch
```

> 关键信息   
> -m, --move  
> Move/rename a branch and the corresponding reflog.
### 如何删除一个分支?

```shell
# 删除一个分支
$ git branch -d my-new-branch

# 强制删除一个分支
$ git branch -D my-new-branch
```

> 关键信息  
> 当被删除的分支存在 '尚未push的commit' 时，  
> 使用 '-d' 参数无法直接删除该分支,     
> 只能使用 '-D' 参数强制删除该分支.  

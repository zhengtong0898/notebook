### 如何将分支推送到远程仓库?
远程可以是 `forked` 的仓库，也可以是 `原始` 的仓库。

&nbsp;  
### 查看 git 仓库
```shell
$ git remote -v
origin          https://github.com/zhengtong0898/abc (fetch)    # forked 仓库
origin          https://github.com/zhengtong0898/abc (push)     # forked 仓库
upstream        https://github.com/MyABC/abc.git (fetch)        # 原始 仓库
upstream        https://github.com/MyABC/abc.git (push)         # 原始 仓库
```

&nbsp;  
### 查看分支
```shell
$ git branch --list
  master
* my-branch
```

&nbsp;  
### 将分支推送到 `forked` 远程仓库
```shell
$ git push --set-upstream origin my-branch
```

&nbsp;  
### 将分支推送到 `原始` 远程仓库
```shell
$ git push --set-upstream upstream my-branch
```

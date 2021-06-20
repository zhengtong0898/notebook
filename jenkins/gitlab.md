### 安装gitlab(Docker版)
```shell script
# 拉取镜像
docker pull gitlab/gitlab-ce

# 启动镜像
docker run --detach --publish 88:80 --name gitlab-example --hostname gitlab-example gitlab/gitlab-ce

# 观察日志
docker logs -f gitlab-example

# 访问gitlab
http://localhost:88/
```

### 取消代理
```shell script
git config --global --unset http.proxy
git config --global --unset https.proxy
```

&nbsp;   
### 设置代理
```shell script
git config --global http.proxy socks5://127.0.0.1:1080
git config --global https.proxy socks5://127.0.0.1:1080
```

&nbsp;   
### 忽略安全证书
```shell script
git -c http.sslVerify=false clone https://gitlab.example.com/USERNAME/PROJECT.git
```

&nbsp;  
### 根据域名和路径来存储账号密码
在一台电脑上, 即要提交到`github`也要提交到`gitlab`, 然而两个仓库的账号并不一样, 这时并不适用全局统一的账号密码, 而是适合使用根据域名和路径来存储账号和密码.
```shell script
git config --global credential.useHttpPath true
```

&nbsp;  
### git 合并提交
方式一: 合并最近连续的提交: 关键词是 rebase 和 squash. [参考这里](https://www.jianshu.com/p/964de879904a)   
方式二: 合并不连续的提交: 关键词是 rebase 和 调整顺序使其连续 和 squash. [参考这里](https://jingyan.baidu.com/article/fcb5aff7f70a61acab4a7167.html)

> 备注:  
> 合并后可能会涉及到 push 操作, 可能需要 push --force .   
> TODO: 是否有完整的操作建议?

&nbsp;  
### git 修改 commit message
方式一: 修改最近一次commit message: git commit --amend.   
方式二: 修改不是最近一次 commit message: 关键词是 rebase 和 reword. [参考这里](https://blog.csdn.net/u013276277/article/details/103608640)


&nbsp;   
### git 如何将 fork repo 的更新同步到我的仓库
git 将仓库分为三个类型:  
类型一: 目标仓库(forked)  
类型二: 我的仓库(remote)  
类型三: 本地仓库(local)  

目标仓库通常是由多人协作的主仓库, 即: 所有人提交的代码最后都会推送到目标仓库.   
代码提交的流程通常是:
1. 我先在自己的电脑上写代码, commit到本地仓库.
2. 提交之前, 想将目标仓库(forked)最新的代码同步到我的仓库(remote),   
   然后再将我的仓库(remote)最新的代码同步到本地仓库(local). 
3. 提交代码到本地仓库(local).
4. push代码到我的仓库(remote).
5. 在我的仓库页面中(remote), new pull request给目标仓库(forked).  


[同步操作参考这里](https://nearsoft.com/blog/how-to-synchronize-your-github-fork/)

&nbsp;  
### TODO
1. git 如何将 fork repo 的更新同步到我的仓库 的流程正确性待验证.   
   需要再多补充一两个链接, 充分说明代码同步操作的正确性.
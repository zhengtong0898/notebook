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
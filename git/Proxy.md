### 如何设置`git`代理?
很多时候`git`访问会非常慢, 这时就有设置代理的需求.

&nbsp;  
### 查看当前代理
```shell
$ git config --global --get http.proxy 
socks5://127.0.0.1:1080

$ git config --global --get https.proxy  
socks5://127.0.0.1:1080
```

&nbsp;  
### 取消代理
```shell
$ git config --global --unset http.proxy
$ git config --global --unset https.proxy
```

&nbsp;  
### 设置代理
```shell
$ git config --global http.proxy socks5://127.0.0.1:1080
$ git config --global https.proxy socks5://127.0.0.1:1080
```
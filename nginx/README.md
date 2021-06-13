### 限制下载速度
nginx.conf 配置文件
```shell script
http {
    limit_rate 200k;          # 限制下载速度.  
}
```

### 版本
Enterprise: 企业版  
OSS(Open Source Software): 开源版

### 安装
[参考资料-1](https://grafana.com/grafana/download) 
```shell
wget https://dl.grafana.com/enterprise/release/grafana-enterprise-8.4.3-1.x86_64.rpm
sudo yum install grafana-enterprise-8.4.3-1.x86_64.rpm
```

### 启动
[参考资料-2](https://www.cnblogs.com/xiao987334176/p/11944558.html)  

默认监听端口: 3000  
默认配置文件: /etc/grafana/grafana.ini

```shell
systemctl enable grafana-server       # 开机自启动grafana服务
systemctl start grafana-server        # 启动grafana服务
```


### 访问

默认账号: admin
默认密码: admin

![img.png](install.png)
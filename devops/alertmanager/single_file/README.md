### 单个文件-单个指标监控

下面列出来的这一组文件是一个单指标监控告警的最小`demo`案例.  
当前案例实现的效果是, 当文件大小100M的70%时, 通过webhook的方式来发送(每5秒发送一次)告警给目标程序.  


> **高亮**    
> 当指标达到阈值时会触发告警(此时告警是fire状态), 只有当指标恢复正常时才会从告警列表中移除.

- [generator.py](./generator.py) 负责持续写入数据到`the_file.txt`文件.  


- [file_exporter.py](./exporter.py) 负责定时读取`the_file.txt`文件大小信息, 然后写入`Gauge`指标对象.


- [hookserver.py](./hookserver.py) 负责启动一个`webserver`监听(`alertmanager`的`webhook`通知的)告警信息.  


- [prometheus.yml](./prometheus.yml) 和 [alert_rule.yml](./alert_rule.yml) 是 **prometheus** 的配置文件.  


- [alertmanager.yml](./alertmanager.yml) 是 **alertmanager** 的配置文件.  



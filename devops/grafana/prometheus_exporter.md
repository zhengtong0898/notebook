> 参考资料  
> [一篇文章带你理解和使用Prometheus的指标](https://frezc.github.io/2019/08/03/prometheus-metrics/)  
> [一图了解Counter和Gauge两种数据指标类型的区别](https://cloud.tencent.com/developer/article/1784538)    


&nbsp;  

|指标类型|描述|
|---|---|
|Counter|可以简单理解为计数器，是个比较简单但又常用的类型。适用于生成请求次数、错误次数等指标。<br/>在写exporter时, prometheus_client提供了Counter指标基类，它仅提供了inc方法，用于做递增操作。|
|Gauge|Gauge是可以任意上下波动数值的指标类型。<br/>例如：机器的CPU使用率，可大可小。|
|Histogram|[柱状图](https://baike.baidu.com/item/%E7%9B%B4%E6%96%B9%E5%9B%BE/1103834?fr=aladdin) |
|Summary|在客户端直接聚合生成的百分位数。|
|Enum|状态切换|


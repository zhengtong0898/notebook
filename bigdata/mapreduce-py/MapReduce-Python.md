### 按书上的操作
```shell
$ cat sample.txt | python3 max_temperature_map.py | python3 max_temperature_reduce.py 
1950    22
1949    111
```


```shell
[root@sandbox-hdp ~]# sudo -u hdfs hadoop fs -mkdir -p /input/ncdc
[root@sandbox-hdp ~]# sudo -u hdfs hadoop fs -mkdir -p /output
[root@sandbox-hdp ~]# sudo -u hdfs hadoop fs -chown -R root /input
[root@sandbox-hdp ~]# sudo -u hdfs hadoop fs -chown -R root /output
[root@sandbox-hdp ~]# hadoop fs -put /root/hadoop-book/input/ncdc/sample.txt /input/ncdc/

[root@sandbox-hdp ~]# hadoop  jar     /usr/hdp/3.0.1.0-187/hadoop-mapreduce/hadoop-streaming-3.1.1.3.0.1.0-187.jar \
                             -input   /input/ncdc/sample.txt \
                             -output  /output/output \
                             -mapper  "python3.6 /home/hdfs/max_temperature_map.py" \
                             -reducer "python3.6 /home/hdfs/max_temperature_reduce.py"
```
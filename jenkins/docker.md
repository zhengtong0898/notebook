# 镜像操作
### 下载一个镜像
```shell
docker pull nginx
```


### 查看镜像列表
```shell
docker images
```


### 删除一个镜像
```shell
image_id=`docker images | awk '/nginx/{print $3}'`
docker rmi $image_id
```


### 在运行中的容器的基础上, 制作一个镜像
```shell
docker pull centos:7
docker run -it --name tmp-centos7 -d centos:7

# 在容器中"安装服务"
docker exec -it tmp-centos7 bash
[root@tmp-centos7 /]# yum install python3
[root@tmp-centos7 /]# vi pythonloop.py
import time

count = 0
while True:
    print(f"pythonloop: {count}...")
    count += 1
    time.sleep(1)

[root@tmp-centos7 /]# exit

# 制作镜像
docker commit -a "zt" -m "安装了python3, 部署了pythonloop程序文件" tmp-centos7 pythonloop:v1

# 启动镜像
docker run -it --name pythonloop-test -d pythonloop:v1 python3 /pythonloop.py

# 查看日志
docker logs -f pythonloop-test
pythonloop: 0...
pythonloop: 1...
pythonloop: 2...
pythonloop: 3...
pythonloop: 4...
pythonloop: 5...
pythonloop: 6...
pythonloop: 7...
pythonloop: 8...
pythonloop: 9...
pythonloop: 10...
```



&nbsp;  
# 容器操作
### 查看容器列表
```shell
docker ps -a
```


### 从镜像中, 运行一个容器
```shell
# -d, --detach: Run container in background and print container ID.  
#       --name: Assign a name to the container.  
docker run --name tmp-nginx-container -d nginx
```

### 从已停止的容器中, 启动一个容器
```shell
# 它会按照 run 时指定的 command 来启动容器.
docker start tmp-nginx-container
```


### 停止一个容器
```shell
container_id=`docker ps | awk '/tmp-nginx-container/{print $1}'`
docker stop $container_id
```

### run 和 start 的区别:  
run: 从镜像中运行一个容器, 通常情况下需指定一个脚本来启动容器内服务.  
start: 从已停止的容器中启动该容器, 它会按照 run 时指定的 command 来启动容器.
> 有效参考  
> [docker容器内服务随容器启动而自启动](https://blog.csdn.net/qq_34661580/article/details/77771717)


### 删除一个容器
```shell
container_id=`docker ps | awk '/tmp-nginx-container/{print $1}'`
docker rm $container_id
```




### 进入容器
```shell
container_id=`docker ps | awk '/tmp-nginx-container/{print $1}'`
docker exec -it $container_id bash

# 帮助文档: docker exec --help
```


### 端口映射
```shell
# 将本地 80 端口映射到容器 'tmp-port-map' 的 8080 端口.
docker run -itp 127.0.0.1:80:8080/tcp --name tmp-port-map -d centos:7  

# 部署程序
docker exec -it tmp-port-map bash
[root@tmp-centos7 /]# yum install vim python3 -y
[root@tmp-centos7 /]# pip3 install tornado==4.5 
[root@tmp-centos7 /]# vim webserver.py
import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8080)
    tornado.ioloop.IOLoop.current().start()

[root@tmp-centos7 /]# python3 webserver.py

# 打开浏览器, 访问 http://localhost, 将会访问 'tmp-port-map' 容器中的 8080 程序服务.
```


### 目录映射
```shell
# -v 是隶属于 run 下面的参数.
# 将本机的 /tmp目录 挂在到 'mount-test'容器的 /tmp目录.
docker run --name mount-test -v /tmp:/tmp -itd centos:7  
```

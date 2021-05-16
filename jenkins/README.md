### 安装Jenkins
操作系统: CentOS 7.6   
安装教程: [Jenkins官网](https://pkg.jenkins.io/redhat-stable/)

- 预备操作
  ```shell script
  yum install vim wget net-tools mlocate git gcc -y
  systemctl stop firewalld
  systemctl disable firewalld
  sed -ie 's/SELINUX=.*/SELINUX=disabled2/g' /etc/selinux/config
  init 6
  ```

- 安装jenkins
  ```shell script
  wget -O /etc/yum.repos.d/jenkins.repo https://pkg.jenkins.io/redhat-stable/jenkins.repo
  rpm --import https://pkg.jenkins.io/redhat-stable/jenkins.io.key
  yum install java-11-openjdk-devel -y
  yum install jenkins -y
  ```
  > 备注:  
  > 执行 yum install jenkins -y 安装完成之后, 会生成一个服务文件.

- 启动Jenkins
  ```shell script
  # 方式一
  java -jar /usr/lib/jenkins/jenkins.war --httpPort=8080
  
  # 方式二
  /etc/init.d/jenkins stop
  /etc/init.d/jenkins start
  ```

- 通过代理启动Jenkins  
  Jenkins 启动后, 在安装向导页面->安装插件页面, 很多插件在安装过程中会出现Read Time Out的情况, 这时就需要为 jenkins 做网络代理.
  ```shell script
  git config --global http.proxy socks5://127.0.0.1:1080
  git config --global https.proxy socks5://127.0.0.1:1080  
  git clone https://github.com/rofl0r/proxychains-ng.git 
  cd proxychains-ng 
  ./configure && make && make install  
  sed -ie "s/socks4 127.0.0.1 9050/socks5 127.0.0.1 1080/g" /usr/local/etc/proxychains.conf
  
  rm -rf ~/.jenkins/
  proxychains4 java -jar /usr/lib/jenkins/jenkins.war --httpPort=8080
  ```  
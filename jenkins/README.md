### 开始之前: 一些术语
|术语|全称| 描述 |
|---|---|---|
|SCM|Source Code Management| [源代码管理平台.](https://intellipaat.com/community/25572/jenkins-scm-what-does-scm-mean-in-jenkins) |
|DSL|Domain Specific Language|[领域特定语言](https://medium.com/tech-learn-share/jenkins-job-dsl-667e88afc2f3), 适用于Pipeline声明式语法.|
|Pipeline|Pipeline|[流水线](https://www.jenkins.io/doc/book/pipeline/#overview)描述的是代码从构建、部署、测试、到产出质量报告的过程. |
|CICD|Continuous Intergration, Continuous Delivery| [持续继承, 持续交付.](https://www.redhat.com/zh/topics/devops/what-is-ci-cd) |


&nbsp;  
> [RedHat 对 CIDCD 的描述](https://www.redhat.com/zh/topics/devops/what-is-ci-cd):    
> CI指的是研发提交代码后, 自动运行基于单元测试的全量回归测试(含当前提交的单元测试), 测试通过后, 自动合并代码.  
> CI解决的是研发中由过多应用分支和冲突问题.    
> CD指的是从代码仓库发布到生产环境的部署过程(产品呈现在目标客户的面前).   
> 
> CIDCD就是强调自动化的过程和自动化的程度, 最终的目的还是为了能够加速软件开发到发布的生命周期的进程, 减少人的工作量.   

&nbsp;  
&nbsp;  
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

&nbsp;  
&nbsp;  
### Tips
[1. 如何切换Jenkins的语言?](./tips/switch_language.md)   
[2. 什么是jenkinsfile?](./tips/jenkinsfile.md)   
[3. 如何生成和添加密钥凭证?](./tips/generate_credential.md)   
[4. 如何添加一个节点?](./tips/new_node.md)   
[5. 如何在指定节点上构建任务?](./tips/choose_node_for_build.md)  

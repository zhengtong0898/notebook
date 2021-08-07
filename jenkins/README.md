### 开始之前: 一些术语
|术语|全称| 描述 |
|---|---|---|
|SCM|Source Code Management| [源代码管理平台.](https://intellipaat.com/community/25572/jenkins-scm-what-does-scm-mean-in-jenkins) |
|DSL|Domain Specific Language|[领域特定语言](https://medium.com/tech-learn-share/jenkins-job-dsl-667e88afc2f3), 适用于Pipeline声明式语法.|
|Pipeline|Pipeline|[流水线](https://www.jenkins.io/doc/book/pipeline/#overview) 描述的是代码从构建、部署、测试、到产出质量报告的过程. |
|CICD|Continuous Intergration, Continuous Delivery| [持续继承, 持续交付.](https://www.redhat.com/zh/topics/devops/what-is-ci-cd) |
|ETA|Estimated Time of Arrival|预计到达时间|
|DDL|Deadline / Due Date|截止时间|
|ETD|Estimated Time of Departure|预计离开时间|
|ETC|Estimated Time of closing|预计关闭时间|
|EOL|End of Life|寿命终止 / 终止维护 / 已死|


&nbsp;  
&nbsp;  
### CICD 是什么?
我根据 [RedHat 对 CIDCD 的描述](https://www.redhat.com/zh/topics/devops/what-is-ci-cd) 和自己的理解，总结出下面这段描述:

&nbsp;  
#### Continuous Integration (持续继承) 
研发提交代码后(提交到forked的仓库), 紧接着要做的是, 将代码 `Pull Request` 推送到主仓库.  
此时自动化任务开始介入, 它负责执行全量的单元测试(称为: 回归测试), 确保这次提交的代码没有破坏原有代码的功能.      
当自动化任务执行结束后, 主仓库代码审查人员就开始进行 `Code Review` 并决定打回或合并代码(思考发散-1).  
当天多个(所有) `Pull Request` 合并完成之后, 会进行统一的集成测试(称为: 流程性测试), 确保各主线功能的流程没有被破坏.      
> CI的目标是: 要做到， 在每一天开始的时候，我们就能从全局的视野去感知当前产品的最新问题清单.


&nbsp;  
#### Continuous Delivery (持续迭代)
当集成测试通过后, 持续迭代需要做的是自动化的将构建好的代码, 打好包放在可发布的位置中.     
打包指的是: 对多平台的自动化编译和打包, 最终为每个平台生成不同的应用程序的安装包.     
可发布的位置指的是: 可以是 git 的 Releases 页面, 也可以是公司内部的共享网络磁盘的指定目录中.   
> CD的目标是: 拥有一个可随时部署到生产环境的代码库.  


&nbsp;  
#### Continuous Deployment (持续部署)
当持续迭代完成后, 我们就有一个可部署的应用程序安装包.  
持续部署就是将该应用程序安装包, 安装到指定的环境完成最终产品的呈现.  
持续部署的过程是: 
1. 检查系统环境: 操作系统内核参数是否满足产品要求、产品依赖的软件和版本是否满足要求.
2. 执行部署: 调整内核参数、升级或安装依赖的软件、解压应用程序安装包、配置配置文件、启动应用程序.
3. 检查应用是否启动成功.  
> CD的目标是: 解决配置文件混乱和错乱的困扰，解决环境不统一的困扰.   


&nbsp;  
&nbsp;  
### Tips
[1. 安装Jenkins](./tips/jenkins_install.md)   
[2. 如何切换Jenkins的语言?](./tips/switch_language.md)       
[3. 如何生成和添加密钥凭证?](./tips/generate_credential.md)   
[4. 如何添加一个节点?](./tips/new_node.md)   
[5. 如何在指定节点上构建任务?](./tips/choose_node_for_build.md)  
[6. 什么是jenkinsfile?](./tips/jenkinsfile.md)  

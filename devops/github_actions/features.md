### Overview

- 静态代码检查、构建、测试、部署  
  > GitHub Actions is a continuous integration and continuous delivery (CI/CD) platform 
  > that allows you to automate your build, test, and deployment pipeline. 
  > You can create workflows that build and test every pull request to your repository, 
  > or deploy merged pull requests to production.  
  > 
  > 当代码`push`到`github`仓库时, 代码会先写入仓库, 然后`github`会默默的拉起一个任务来跑定制好的工作流, 这样我们就可以观测这次提交的情况.    
  > 当仓库接收到`pull_request`请求时, 代码会先进入`Pull requests`列表页面, 然后`github`会默默的拉起一个任务来跑定制好的工作流, 这样提交人可以根据执行失败情况来做修改.
  
- 为`issue`自动创建标签
  > GitHub Actions goes beyond just DevOps and lets you run workflows when other events 
  > happen in your repository. For example, you can run a workflow to automatically add 
  > the appropriate labels whenever someone creates a new issue in your repository.  
  >
  > 当创建`issue`时, 也可以触发一个任务来跑制定好的标签流程.  

- 机器
  > GitHub provides Linux, Windows, and macOS virtual machines to run your workflows, 
  > or you can host your own self-hosted runners in your own data center or cloud infrastructure.
  > 
  > `GitHub`提供了虚拟机来运行这些工作流任务, 我们也可以自己提供虚拟机并暴露公网接口即可.  


&nbsp;  
### 工作流的组成  

- 一个工作流可以包含一个或多个`jobs`  
  > Your workflow contains one or more jobs which can run in sequential order or in parallel.  
  > 
  > 每个任务都是独立的, 并且`github action`执行这些任务是并行执行的.  
  > 当我们需要同时在不同的平台上执行任务时, 就定义多个`jobs`.  

- 一个`job`必须指定一个虚拟机  
  > Each job will run inside its own virtual machine runner, or inside a container.  
  > 
  > 由于每个`job`都是一个完整、独立的事物, 因此都需要制定一个虚拟机, `github_action`会帮你从0到1开始执行.  

- 一个`job`可以包含一个或多个`steps`
  > Each job has one or more steps that either run a script that you define or run 
  > an action, which is a reusable extension that can simplify your workflow.  
  > 
  > 每个`step`可以运行一个系统命令或一个脚本, `github_action`提供了`run`关键字可以重复执行多个`step`, 简化工作流的定义.   

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

- **workflows**  
  `github`要求所有个工作流描述文件都要存放在`.github/workflows`目录下.  
  一个仓库可以包含多个工作流描述文件, 每个工作流文件可以做不同的任务, 例如:  
  一个工作流文件专门处理当`pull request`时, 执行构建、测试.  
  一个工作流文件专门处理当`release`时, 执行部署等.  


- **Events**  
  `pull request`、`open an issue`、`push a commit`、`schedule` 这些事件都作为出发执行工作流的条件.  


- **jobs**  
  一个工作流可以包含一个或多个`jobs`  
  > Your workflow contains one or more jobs which can run in sequential order or in parallel.  
  > 
  > 每个任务都是独立的, 并且`github action`执行这些任务是并行执行的.  
  > 当我们需要同时在不同的平台上执行任务时, 就定义多个`jobs`.  


- **runner**  
  一个`job`必须指定一个虚拟机(runner)  
  > Each job will run inside its own virtual machine runner, or inside a container.  
  > 
  > 由于每个`job`都是一个完整、独立的事物, 因此都需要制定一个虚拟机, `github_action`会帮你从0到1开始执行.  


- **steps**
  一个`job`可以包含一个或多个`steps`
  > Each job has one or more steps that either run a script that you define or run 
  > an action, which is a reusable extension that can simplify your workflow.  
  > 
  > 每个`step`可以运行一个系统命令或一个脚本, `github_action`提供了`run`关键字可以重复执行多个`step`, 简化工作流的定义.   


- **actions**  
  `uses`关键字可以使用`github`上的`action`, 例如: `uses: actions/checkout@v3`  
  > `run`允许我们直接运行一个`shell`命令, 也允许我们运行一个脚本.  
  > 如果说`脚本`是对`run`的封装, 那么运行`action`就是对`脚本`的封装.  

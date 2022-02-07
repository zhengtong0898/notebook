### 参与者(actor)
参与者是在系统之外与系统交互的某人或某事物, page-43, [参考-1](https://plantuml.com/zh/sequence-diagram#5d2ed256d73a7298)  
- [actor.plantuml](plant_umls/actor.plantuml)
  ```plantuml
  @startuml
  'actor 是一个专有单词, 用于表示参与者. 
  actor ZhangSan
  ZhangSan -> System: 访问
  ZhangSan <- System: 返回
  @enduml
  ```
- [actor.png](plant_umls/actor.png)
  <p align="center">
    <img src="plant_umls/actor.png">
  </p>

&nbsp;  
&nbsp;  
### 给自己发消息  
参与者可以给自己发信息, [参考-1](), [参考-2](https://forum.plantuml.net/6180/message-displayed-standard-immediately-before-deactivate).   

- [msg2self.plantuml](plant_umls/msg2self.plantuml)
  ```plantuml
  @startuml
  fibonacci->fibonacci: 递归调用
  @enduml
  ```

- [msg2self.png](plant_umls/msg2self.png)  
  <p align="center">
    <img src="plant_umls/msg2self.png">
  </p>


- [recursion_complex.py](../algorithms/wz-course/essence/recursion_complex.py#L7)  
  ```python3
  def fibonacci(n: int) -> int:
      if n == 0:
          return 0
      elif n == 1:
          return 1
      else:
          return fibonacci(n - 1) + fibonacci(n -2)
  ```

&nbsp;  
&nbsp;  
### 生命线的激活和撤销  
关键字`activate`和`deactivate`用来表示`参与者`一次完整的生命活动.  
- [activate.plantuml](plant_umls/activate.plantuml)
  ```plantuml
  @startuml
  participant User

  User -> A: DoWork-1(重点)
  activate A

  A -> B: << createRequest >>
  activate B

  B -> C: DoWork-1
  activate C
  C --> B: WorkDone
  destroy C

  B --> A: RequestCreated
  deactivate B

  A -> User: Done
  deactivate A

  User -> A: DoWork-2(重点)
  activate A
  A -> A: call self
  A -> User: Done
  deactivate A

  @enduml
  ```
- [activate.png](plant_umls/activate.png)  
  <p align="center">
    <img src="plant_umls/activate.png">
  </p>


&nbsp;  
&nbsp;  
### 关联关系(Association)
TODO: 待补充


&nbsp;  
&nbsp;  
### 依赖关系(Dependency)  
TODO: 待补充

&nbsp;  
&nbsp;  
### 实现关系(Realize)
TODO: 待补充

&nbsp;  
&nbsp;  
### 精化关系(Refine)
TODO: 待补充

&nbsp;  
&nbsp;  
### 聚合关系(Aggregation)
TODO: 待补充

&nbsp;  
&nbsp;  
### 组合关系(Composition)  
TODO: 待补充

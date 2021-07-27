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
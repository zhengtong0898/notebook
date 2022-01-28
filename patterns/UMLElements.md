### 参与者  
UML遵循以人为本的原则, 系统的每个动作都由参与者(**actor**)来触发.  
参与者(**actor**)是在系统之外与系统交互的人或物.  

&nbsp;  
##### 谁是参与者?  

场景1:  
小王到银行去开户, 向大厅经理询问了办理手续, 填写了表单并交给柜台职员, 最终拿到了银行存折.

系统之外: 小王(参与者);  
系统之内: 银行场所、大厅经理、柜台职员、保安、电脑、桌子、椅子等等,  
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; 
由于大厅经理和柜台职员"参与"了场景中的业务, 它们被称为业务工人(**business worker**).  

&nbsp;  
场景2:  
每天自动统计网页访问量, 生成统计报表, 并发送至管理员信箱.  

系统之外: 定时任务(参与者);  
系统之内: 自动统计网页访问量的程序、自动生成统计报表的程序、自动发送邮件给管理员的程序.  

> 这两个案例表明, 参与者可以是人, 也可以是物,   
> 其中物可以是另外一个系统、一个定时器(定时任务)或一个传感器等等.  


&nbsp;  
##### 发现参与者  
场景1:  
机票购买者通过登录到网站购买机票.  

系统之外: 机票购买者(参与者).  
系统之内: 订票网站.  

&nbsp;  
场景2:  
机票购买者通过呼叫中心, 由人工坐席操作订票系统来购买机票.  

系统之外: 机票购买者(不是参与者)、人工坐席(参与者).  
系统之内: 订票系统.   

&nbsp;  
场景3:  
机票购买者通过呼叫中心的自动语音来预定机票.   

系统之外: 机票购买者(不是参与者)、语音呼叫系统(参与者).  
系统之内: 订票系统.   

&nbsp;  
场景4:  
如果电话自动语音是机票预定系统的一个子系统、电话人工坐席也是机票预定系统的一个子系统.  
机票购买者通过呼叫中心的自动语音来预定机票.   
机票购买者通过呼叫中心的人工坐席来预定机票.  

系统之外: 机票购买者(参与者).   
系统之内: 订票系统、电话自动语音子系统、电话人工坐席子系统.  


&nbsp;  
&nbsp;  
### 边界  
面向对象里, 任何一个对象都有一个边界, 外界只能通过这个边界来认识对象, 与对象打交道, 而对象内部则是一个进去.  
我们把边界放大了看, 这个世界上任何一种东西我们都不可能知道它本质上是什么, 而只能通过它的行为、外观、性质来  
描述它是一个什么东西, 行为也好, 外观也罢, 这就是这个东西的一个边界, 我们就是通过边界来认识事物的.  

> 比如说我们观察并描述一幢建筑物, 如果我们的位置在楼的正前方, 能够观察到的东西是大门、招牌、楼层数这些东西;  
> 如果我们的位置是在大厅里, 能够观察到的东西是吊灯、沙发、柱子这些东西;   
> 如果我们的位置是在楼顶上, 能观察到的东西是围栏、烟道、中央空调水冷器这些东西了.  
> 
> 虽然这些东西完全不一样, 但是我们一直都在描述同一幢建筑. 为了更接近真相,   
> 我们能够做的就是不断变换边界, 从更多的侧面去描述同一个信息, 以求最大程度地符合真实的需求.  

在实际工作中应当学会灵活地使用边界, 用边界来决定抽象层次和视角, 进而排除边界外大量的杂音来降低复杂度.  


&nbsp;  
&nbsp;  
### 分析类  
分析类是一个概括词汇, 它由[三个类构成:](https://stackoverflow.com/a/17028825) 边界类(Boundary)、控制类(Control)、实体类(Entity).  
分系类的三高: 
- 高于设计实现
- 高于语言实现
- 高于实现方式


&nbsp;  
&nbsp;  
### 关系

##### 关联关系(association)  
一对一、一对多、多对多, 这种关系都被称为[关联关系](https://faun.pub/association-aggregation-composition-python-ec9947832cbd), 采用 `一条直线` 表示双向"知道"对象的存在.  
关联关系是一种静态(即: 强关联)关系.  
> 根据`Django ORM`的操作,   
> [一对一](https://docs.djangoproject.com/en/4.0/topics/db/examples/one_to_one/) 采取成员变量(`models.OneToOneField`)来获得, 成员变量对象的生命周期随主对象结束而结束.  
> [一对多和多对多](https://docs.djangoproject.com/en/4.0/topics/db/examples/many_to_one/) 采取中间对象(`TableName_set`)来获得, 成员变量对象的生命周期随主对象结束而结束.  



&nbsp;  
##### 依赖关系(dependency)  
依赖关系是一种临时性(弱)的关系, 它通常是运行期产生, 采用 虚线带箭头(`A--->B`)表示`A`依赖`B`.  

```python3
# 这个代码表示A这个类依赖B
class B:
    def __str__(self):
        return "boom"


class A:
    
    def work_with(self, b: B):         # A类依赖B类
        print(b)

a = A()
a.work_with(b=B())
```

&nbsp;  
##### 包含关系(include)
TODO: 找到python3的表达方式.  

&nbsp;  
##### 实现关系(realize)
TODO: 找到python3的表达方式.  

&nbsp;  
##### 聚合关系(aggregation)  
聚合关系 用直线带空心菱形(`A<>——B`)表示`B`聚合到`A`上, 即: `A`由`B`组成.   
聚合关系表达整体由部分构成, 整体和部分不是强依赖的, 即使整体不存在了, 部分仍然存在.  

```python3
# 来源
# https://faun.pub/association-aggregation-composition-python-ec9947832cbd
# https://gist.githubusercontent.com/sohaib-dev/d65a8d61be4cf5b529cba826703a5d96/raw/fee8cd8c804af63e3cc581e33e2c3c7cb98553c3/aggregation.py
class Student:

    def __init__(self, id):
        self._id = id

    def registration_number(self, department_id) -> str:
        return str(self._id) + '-' + department_id


class Department:

    def __init__(self, id, student):
        self._id = id
        self._student = student

    def student_registration(self):
        return self._student.registration_number(self._id)


if __name__ == '__main__':
    student = Student(10)
    department = Department('ENG', student)
    print(department.student_registration())


```


&nbsp;  
##### 组合关系(composition)  
组合关系 用直线实心菱形(`A<>——B`)表示`B`组合成`A`, 即: `A`由`B`组成.  
组合关系表达整体拥有部分的, 是强依赖的关系, 如果整体不存在了, 部分也将消亡.  

```python3
# 来源
# https://faun.pub/association-aggregation-composition-python-ec9947832cbd
# https://gist.githubusercontent.com/sohaib-dev/04c670df1733e80764c217feb69761d6/raw/d96e720244739cd09898ea329da287ea4932a794/composition.py
class Student:

    def __init__(self, id):
        self._id = id

    def registration_number(self, department_id) -> str:
        return str(self._id) + '-' + department_id


class Department:

    def __init__(self, department_id, student_id):
        self._id = department_id
        self._student = Student(student_id)

    def student_registration(self):
        return self._student.registration_number(self._id)


if __name__ == '__main__':
    department = Department('ENG', 10)
    print(department.student_registration())
```

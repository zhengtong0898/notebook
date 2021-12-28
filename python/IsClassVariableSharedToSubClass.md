### 父类的类变量是否共享给所有派生类?
**结论是:** 会继承给所有派生类, 但不会共享给所有派生类.

&nbsp;  
### 继承给所有派生类
假设`Parent`类中有一个`items`类变量, 如果`Child`类继承了`Parent`类.  
即便`Child`不定义`items`类变量, 它也会拥有`items`类变量并且与`Parent.items`是相同的, 这就是继承.   
```python3
class Parent:
    items = {"parent": "parent"}


class Child(Parent):
    pass


if __name__ == '__main__':
    print(f"Child.items: {Child.items}")                # Child.items: {'parent': 'parent'}
    print(f"Parent.items: id: {id(Parent.items)}")      # 140569815771264
    print(f"Child.items: id: {id(Child.items)}")        # 140569815771264

```
**小结:**  
继承的意思是, 创建派生类的时候, 会浅拷贝一份父类的方法和变量给派生类.  


&nbsp;  
### 外部修改派生类的类变量会影响父类的类变量  
```python3
class Parent:
    items = {"parent": "parent"}


class Child(Parent):
    pass


if __name__ == '__main__':
    Child.items["child"] = "child"
    print(f"Parent.items: {Parent.items}")              # Parent.items: {'parent': 'parent'}
    print(f"Child.items: {Child.items}")                # Child.items: {'parent': 'parent', 'child': 'child'}   关键点
    print(f"Parent.items: id: {id(Parent.items)}")      # 140569815771264
    print(f"Child.items: id: {id(Child.items)}")        # 140569815771264

```



&nbsp;  
### 派生类内部无法修改父类的类变量, 只能覆盖父类的类变量
```python

class Parent:
    items = {"parent": "parent"}


class Child(Parent):
    items = {"child": "child"}          # 覆盖父类的类变量


if __name__ == '__main__':
    print(f"Parent.items: {Parent.items}")              # Parent.items: {'parent': 'parent'}
    print(f"Child.items: {Child.items}")                # Child.items: {'child': 'child'}
    print(f"Parent.items: id: {id(Parent.items)}")      # 140518270134720
    print(f"Child.items: id: {id(Child.items)}")        # 140518271047424
```

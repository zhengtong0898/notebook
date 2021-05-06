#ifndef __LINEARLIST_H__
#define __LINEARLIST_H__
#include <iostream>


template<class T>
class LinearList {
public:

    // 析构函数.
    virtual
    ~LinearList() {};

    // 判断当前线性表是否为空.
    virtual bool
    empty() const = 0;

    // 获取当前线性表元素个数.
    virtual int
    size() const = 0;

    // 根据实参: int索引, 获取对应的元素.
    virtual T&
    get(int the_index) const = 0;

    // 根据实参： T&元素, 获取元素的索引.
    virtual int
    index_of(const T& the_element) const = 0;

    // 根据实参: int索引, 删除对应的元素.
    virtual void
    erase(int the_index) = 0;

    // 根据实参1: int 索引, 实参2: T&元素; 把实参2插入到实参1指定的位置.
    virtual void
    insert(int the_index, const T& the_element) = 0;

    // 将线性表打印出来.
    virtual void
    output(std::ostream & out) const = 0;

};

#endif
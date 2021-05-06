#ifndef __CHAINLIST_H__
#define __CHAINLIST_H__
#include "linearlist.h"
#include <iostream>
#include <string>


template<class T>
struct ChainNode {

    // 数据
    T element;

    // 链条
    ChainNode<T>* next;

    // 空的构造函数
    ChainNode();

    // 构造函数
    ChainNode(const T& element) {
        this->element = element;
        this->next = nullptr;
    }

    // 构造函数
    ChainNode(const T& element, ChainNode<T>* next) {
        this->element = element;
        this->next = next;
    }

};


template<class T>
class Chain: public LinearList<T> {
protected:
    ChainNode<T>* first_node;
    int list_size;

    void check_index(int the_index) const;

public:
    Chain(int init_capacity = 10);
    Chain(const Chain<T> & other_chain);
    ~Chain();

    virtual bool
    empty() const;

    virtual int
    size() const;

    virtual T&
    get(int the_index) const;

    virtual int
    index_of(const T& the_element) const;

    virtual void
    erase(int the_index);

    virtual void
    insert(int the_index, const T& the_element);

    virtual void
    output(std::ostream& out) const;

};


template<class T>
Chain<T>::Chain(int init_capacity) {
    if (init_capacity < 1) throw std::runtime_error("init_capacity must be > 0");
    first_node = nullptr;
    list_size = 0;
}


template<class T>
Chain<T>::Chain(const Chain<T>& other_chain) {
    list_size = other_chain.list_size;                                  // 常量类型, 深度复制.

    if (list_size == 0) {
        first_node = nullptr;
        return void();
    }

    first_node = new ChainNode<T>(other_chain.first_node->element);     // first_node 指针, 指向 匿名new 对象, 深度复制.
    ChainNode<T>* source_node = other_chain.first_node->next;           // source_node 指针, 指向 other_chain.first_node->next 对象;
    ChainNode<T>* target_node = first_node;                             // target_node 指针, 指向 first_node 对象;

    // source_node 在这里充当一个临时变量交换的作用.
    // target_node 在这里充当一个临时变量交换的作用.
    while (source_node != nullptr) {
        target_node->next = new ChainNode<T>(source_node->element);     // new一个对象出来存储到 target_node->next 中, 这是深度复制.
        target_node = target_node->next;                                // 进入到下一个 target_node 链条节点
        source_node = source_node->next;                                // 进入到下一个 source_node 链条节点
    }

    target_node->next = nullptr;
}


template<class T>
Chain<T>::~Chain() {

    // next_node 在这里充当一个临时变量交换的作用.
    while (first_node != nullptr) {
        ChainNode<T>* next_node = first_node->next;
        delete first_node;
        first_node = next_node;
    }

}


template<class T>
void Chain<T>::check_index(int the_index) const {
    if (the_index < 0) throw std::runtime_error("param: the_index must be >= 0");
    if (the_index >= list_size) throw std::runtime_error("param: the_index must be < " + std::to_string(list_size));
}


template<class T>
bool Chain<T>::empty() const {
    return list_size == 0;
}


template<class T>
int Chain<T>::size() const {
    return list_size;
}


template<class T>
T& Chain<T>::get(int the_index) const {

    // current_node 在这里充当一个临时变量交换的作用.
    ChainNode<T>* current_node = first_node;
    for (int i = 0; i < the_index; ++i) {
        current_node = current_node->next;
    }

    return current_node->element;

}


template<class T>
int Chain<T>::index_of(const T& the_element) const {

    int index = 0;

    // current_node 在这里充当一个临时变量交换的作用.
    ChainNode<T>* current_node = first_node;
    while (true) {
        if (current_node == nullptr) break;
        if (current_node->element == the_element) break;

        current_node = current_node->next;
        index += 1;
    }

    if (current_node == nullptr) return -1;
    return index;
}


template<class T>
void Chain<T>::erase(int the_index) {

    this->check_index(the_index);

    // 预处理了一次.
    ChainNode<T>* previous_node = first_node;
    ChainNode<T>* current_node = first_node->next;

    if (the_index == 0) {
        first_node = current_node;
        current_node = previous_node;
    } else {
        // 上面预处理了一次, 所以这里 the_index 要减去一次.
        for (int i = 0; i < the_index - 1; ++i) {
            previous_node = current_node;
            current_node = current_node->next;
        }

        // 重新链接
        previous_node->next = current_node->next;
    }

    // 删除节点
    delete current_node;

    // 递减节点数量
    --list_size;
}


template<class T>
void Chain<T>::insert(int the_index, const T& the_element) {
    if (the_index < 0) throw std::runtime_error("param: the_index must be >= 0");
    if (the_index > list_size) throw std::runtime_error("param: the_index must be < " + std::to_string(list_size));

    ChainNode<T>* insert_node = new ChainNode<T>(the_element);
    if (the_index == 0) {
        first_node = insert_node;
    } else {
        ChainNode<T>* previous_node = first_node;
        ChainNode<T>* current_node = first_node->next;

        for (int i = 0; i < the_index - 1; ++i) {
            previous_node = current_node;
            current_node = current_node->next;
        }

        previous_node->next = insert_node;
        insert_node->next = current_node;
    }

    ++list_size;
}


template<class T>
void Chain<T>::output(std::ostream& out) const {
    for (ChainNode<T>* current_node = first_node;
                       current_node != nullptr;
                       current_node = current_node->next) {
        out << current_node->element << std::endl;
    }
}


template<class T>
std::ostream& operator<<(std::ostream& out, const Chain<T>& x) {
    x.output(out);
    return out;
}


#endif // !__CHAINLIST_H__

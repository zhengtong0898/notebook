#ifndef __ARRAYLIST_H__
#define __ARRAYLIST_H__
#include "linearlist.h"

template<class T>
class ArrayList : public LinearList<T> {
protected:
    void
    check_index(int the_index) const;

    T* element;
    int array_length;                   // 数组总数量
    int list_size;                      // 已插入元素数量

public:
    ArrayList(int init_apacity = 10);
    ArrayList(const ArrayList<T>&);
    ~ArrayList() { delete[] element; }

    virtual bool empty() const;
    virtual int size() const;
    virtual T& get(int the_index) const;
    virtual int index_of(const T& element) const;
    virtual void erase(int the_index);
    virtual void insert(int the_index, const T& the_element);
    virtual void output(std::ostream& out) const;

    int capacity() const;
};

#endif

#include "arraylist.h"
#include <iostream>
#include <iterator>
#include <vector>
#include <exception>
#include <algorithm>
#include <string>
#include <assert.h>


/**********************************************************************************************************************
 * 线性表--数组描述
 *
 * 数组的特点:
 *     1. 内存连续性
 *        new一个固定大小的内存, 该内存是一块连续性的内存.
 *
 *     2. 支持随机访问元素
 *        给定一个索引位置可直接返回该位置的值;                                              时间复杂度: O(1).
 *
 *     3. 最优写入(当前代码样例并没有提供: push_back)
 *        在数组中最后一个有效值的下一个位置写入是最优操作, 因为这样操作不需要移动其他元素.      时间复杂度: O(1)
 *
 *     4. 最差写入
 *        在数组中的第一个位置插入一条数据, 那么所有元素都要往后移动一个位置.                   时间复杂度: O(n)
 *
 *     5. 最优移除/最差移除 与 最优写入和最差写入是相同道理.
 *
 *
 * 这就是 ArrayList 的数据结构特征和原理.
 **********************************************************************************************************************/
namespace {

    template<class T>
    void change_length(T*& a, int old_length, int new_length) {
        if (new_length < 0)
            throw std::runtime_error("new length must be >= 0");

        T* temp = new T[new_length];
        int number = std::min(old_length, new_length);
        std::copy(a, a + number, temp);
        delete[] a;
        a = temp;
    }

}


template<class T>
ArrayList<T>::ArrayList(int init_capacity) {
    if (init_capacity < 1) throw std::runtime_error("init_capacity must be > 0");
    array_length = init_capacity;
    element = new T[array_length];
    list_size = 0;
}


template<class T>
ArrayList<T>::ArrayList(const ArrayList<T>& the_list) {
    array_length = the_list.array_length;
    list_size = the_list.list_size;
    element = new T[array_length];
    std::copy(the_list.element, the_list.element + list_size, element);
}


template<class T>
bool ArrayList<T>::empty() const {
    return list_size == 0;
}


template<class T>
int ArrayList<T>::size() const {
    return list_size;
}

template<class T>
void ArrayList<T>::check_index(int the_index) const {
    if (the_index < 0) throw std::runtime_error("param: the_index must be >= 0");
    if (the_index >= list_size) throw std::runtime_error("param: the_index must be < " + std::to_string(list_size));
}


/*
 * 由于数组支持随机访问, 因此这里直接通过分片就可以拿到对应的值, 时间复杂度O(1).
 */
template<class T>
T& ArrayList<T>::get(int the_index) const {
    // 边界检查: 0 <= the_index < list_size
    this->check_index(the_index);
    return element[the_index];
}


template<class T>
int ArrayList<T>::index_of(const T& the_element) const {
    // find 如果没有找到, 那么返回的是 element 的最后一个元素的下一个元素的地址.
    T * value_address = std::find(element, element + list_size, the_element);

    // 指针-指针 = 索引.
    // 第一个有效索引是 0,
    // 最后一个有效索引是 list_size -1;
    int distance = value_address - element;

    // 如果索引 == list_size, 那么表示 std::find 没有找到元素,
    // 所以返回最后一个元素的下一个元素的地址, 用于表示没有找到.
    bool not_found = distance == list_size;
    if (not_found) distance = -1;
    return distance;
}


template<class T>
void ArrayList<T>::erase(int the_index) {
    // 边界检查: 0 <= the_index < list_size
    check_index(the_index);

    // 假设:
    // the_index = 2;
    // list_size = 10;
    //
    // 那么:
    // 第一个参数: element + the_index + 1;      等同于  element + 3;
    // 第二个参数: element + list_size;          等同于  element + 10;
    // 第三个参数: element + the_index;          等同于  element + 2;            从这里开发复制
    //
    // std::copy 是从做往右复制.
    //
    // 所以:
    // element[3] 赋值给 element[2];
    // element[4] 赋值给 element[3];
    // element[5] 赋值给 element[4];
    // element[6] 赋值给 element[5];
    // element[7] 赋值给 element[6];
    // element[8] 赋值给 element[7];
    // element[9] 赋值给 element[8];
    std::copy(element + the_index + 1, element + list_size, element + the_index);

    // --list_size;       递减一个数值, 表示列表元素减少了一个, 返回递减后的值.
    // element[xx].~T();  销毁最后一个值的对象, 对象被销毁了, 但是内存地址仍然是有效的已分配内存, 可以再次写入相同类型的值.
    element[--list_size].~T();
}


template<class T>
void ArrayList<T>::insert(int the_index, const T& the_element) {
    if (the_index < 0) throw std::runtime_error("param: the_index must be >= 0");

    // 如果数组满了, 那么就在这里扩容.
    if (list_size == array_length) {
        change_length(element, array_length, 2 * array_length);
        array_length *= 2;
    }

    // 假设:
    // the_index == 2;
    // list_size = 10;
    //
    // 那么:
    // 有效索引范围是: 0 -- 9;
    // 第一个参数: element + the_index;      等同于 element + 2;
    // 第二个参数: element + list_size;      等同于 element + 10;
    // 第三个参数: element + list_size + 1;  等同于 element + 11;
    //
    // 有过编码经验都知道由于索引是从0开始的, 所以第二个参数在程序执行过程中内部是会自动-1的;
    // std::copy_backward 函数是从右向左复制, 所以第三个参数也是要自动-1的;
    //
    // 所以:
    // element[9] 赋值给 element[10]       // 当 list_size < array_length 时, 这个值被扔进黑洞了;
    //                                    // 当 list_size == array_length 时, 这是有效赋值, 因为前面执行了扩容操作.
    // element[8] 赋值给 element[9]
    // element[7] 赋值给 element[8]
    // element[6] 赋值给 element[7]
    // element[5] 赋值给 element[6]
    // element[4] 赋值给 element[5]
    // element[3] 赋值给 element[4]
    // element[2] 赋值给 element[3]
    //
    // element[2] 的值不变;
    // element[1] 的值不变;
    // element[0] 的值不变;
    std::copy_backward(element + the_index, element + list_size, element + list_size + 1);

    // 将新的值写入到 element[2];
    element[the_index] = the_element;

    // 已插入元素 + 1;
    list_size++;
}


template<class T>
void ArrayList<T>::output(std::ostream& out) const {
    std::copy(element, element + list_size, std::ostream_iterator<T>(out, "  "));
}


template<class T>
std::ostream& operator<<(std::ostream& out, const ArrayList<T>& x) {
    x.output(out);
    return out;
}



int main()
{
    // 实例化
    ArrayList<int> array_list(10);
    std::cout << "array_list.empty: " << array_list.empty() << std::endl;                   // array_list.empty: 1
    std::cout << "array_list.size: " << array_list.size() << std::endl;                     // array_list.size: 0

    // 写入数据
    array_list.insert(0, 2);
    array_list.insert(1, 4);
    array_list.insert(2, 6);
    array_list.insert(3, 8);
    array_list.insert(4, 10);
    array_list.insert(5, 11);
    array_list.insert(6, 13);
    array_list.insert(7, 15);
    array_list.insert(8, 17);
    array_list.insert(9, 19);

    std::cout << "\n\n" << std::endl;
    std::cout << "array_list.empty: " << array_list.empty() << std::endl;                   // array_list.empty: 0
    std::cout << "array_list.size: " << array_list.size() << std::endl;                     // array_list.size: 10

    // 获取索引
    std::cout << "\n\n" << std::endl;
    int index = array_list.index_of(13);
    std::cout << "array_list.index_of(13): " << index << std::endl;                         // array_list.index_of(13): 6

    // 按索引来删除元素
    std::cout << "\n\n" << std::endl;
    array_list.erase(index);
    std::cout << "array_list.erase(13). " << std::endl;                                     // array_list.erase(13).

    // 获取索引
    std::cout << "\n\n" << std::endl;
    index = array_list.index_of(13);
    std::cout << "array_list.index_of(13): " << index << std::endl;                         // array_list.index_of(13): -1
}

#include "arraylist.h"


void test_arraylist(void) {
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

# 冒泡排序
# 原理: https://www.bilibili.com/video/BV1Zz4y1D7ZE/?spm_id_from=trigger_reload
import random


def loop_for_swap_v1(items, sorted_count: int) -> (bool, int, int):
    swapped = False
    swapped_count = 0
    looped_count = 0

    valid_len = len(items) - sorted_count
    for current_index in range(valid_len - 1):              # - 1, 是为了保护边界取值异常.
        looped_count += 1
        next_index = current_index + 1
        if items[current_index] > items[next_index]:
            swapped = True
            swapped_count += 1
            items[current_index], items[next_index] = items[next_index], items[current_index]

    return swapped, swapped_count, looped_count


def loop_for_swap_v2(items, sorted_count: int) -> (bool, int, int):
    swapped = False
    swapped_count = 0
    looped_count = 0

    valid_len = len(items) - sorted_count
    for current_index in range(valid_len):
        looped_count += 1
        next_index = min(current_index + 1, valid_len - 1)  # 取最小值
        if items[current_index] > items[next_index]:
            swapped = True
            swapped_count += 1
            items[current_index], items[next_index] = items[next_index], items[current_index]    # swap here

    return swapped, swapped_count, looped_count


def bubble_sort_linear(items):
    # 每次一级循环要求将一个对象排序到右侧, 所以最坏情况下需要执行 len(items) 次.
    for i in range(len(items)):
        swapped, swapped_count, looped_count = loop_for_swap_v1(items, sorted_count=i)
        if not swapped: break                    # 没有交换任何数据, 表示整个列表已排序完毕
    return items


if __name__ == '__main__':
    collection = random.sample(range(-50, 50), 50)
    sorted_collection = sorted(collection)
    assert bubble_sort_linear(collection) == sorted_collection

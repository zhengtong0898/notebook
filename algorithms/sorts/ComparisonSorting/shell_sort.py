# 希尔排序
# 原理:  https://www.bilibili.com/video/av94596268
#       https://www.pythonpool.com/shell-sort-python/
#       https://www.programiz.com/dsa/shell-sort
# 参考: https://www.geeksforgeeks.org/python-program-for-shellsort/
# 时间复杂度: Average-O(nlog n)    Worst-O(n2)     Best-O(nlog n)    Space-O(1)    Stability-No
import random


def shell_sort(items):
    n = len(items)
    gap = n // 2

    while gap > 0:

        # range(gap, n) -> 遍历右侧元素.
        # 由于 n // 2, 左侧元素要么等于右侧元素,
        # 要么小于右侧元素, 因此这里选择遍历右侧元素.
        for r_index in range(gap, n):

            r_value = items[r_index]

            # l_index 是一个游标.
            # 隐藏信息: 它是一个偏移的游标, 它需要 - gap 才能得到正确的左侧索引值.
            l_index = r_index
            while True:

                # 处理越界防护 -> items[l_index - gap].
                if l_index < gap:
                    break

                # 排序正确, 不做任何动作, 跳出循环.
                l_value = items[l_index - gap]
                if l_value <= r_value:
                    break

                # 当左大右小时, 代码会来到这里,
                # 执行: 将左侧大的值写入到右侧位置.
                #
                # 隐藏信息-1: 此时左侧大的值并没有被销毁, 即: items[l_index - gap] 仍然存在.
                #            l_index -= gap 会将索引位置计算出来, 交给后续的 items[l_index] = r_value 来完成交换动作.
                #
                # 隐藏信息-2: 当 (l_index - gap) >= gap 时, r_value 需要跟不同gap位置的元素进行比较和交换位置.
                items[l_index] = items[l_index - gap]
                l_index -= gap

            # 将右侧小的值写入到左侧空槽位置.
            items[l_index] = r_value

        gap //= 2


if __name__ == '__main__':
    collection = [5, 4, 3, 2, 1]
    sorted_collection = sorted(collection)
    shell_sort(collection)
    assert collection == sorted_collection

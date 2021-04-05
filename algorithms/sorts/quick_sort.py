# 快速排序
# 原理: https://www.bilibili.com/video/BV1at411T75o?from=search&seid=16200417356150128649
import random
import logging
logger = logging.getLogger("quick_sort")


def quick_sort_linear(items: list, typo="root_") -> list:
    if len(items) < 2: return items              # 递归保护边界取值异常

    pivot = items.pop()
    left, right = [], []

    for item in items:
        (right if item > pivot else left).append(item)

    logger.debug("typo(in):  %s;    values: %s" % (typo, (left, [pivot], right)))
    result = quick_sort_linear(left, "left_") + [pivot] + quick_sort_linear(right, "right")
    logger.debug("typo(out): %s;    values: %s" % (typo, result))
    return result


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    collection = random.sample(range(-30, 30), 30)
    sorted_collection = sorted(collection)
    assert quick_sort_linear(collection) == sorted_collection
    # collection = [2, -1, 6, -10, -8, -4, -9, 8, 4, -3]
    # quick_sort_linear(collection)

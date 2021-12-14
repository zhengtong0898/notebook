import uuid


def recursion(n: int) -> int:
    """
    最简单的递归例子

       递归采取的策略是先层层递进的走到最低层,
    当满足递进终止条件时再层层回归的走到最顶层.
    以当前代码为例, 假设 n = 5;
    先层层递进: 5 - 1 = 4    (第一层)
              4 - 1 = 3    (第二层)
              3 - 1 = 2    (第三层)
              2 - 1 = 1    (第四层)        符合递进终止条件

    后层层回归: 1 + 3 = 4    (第四层)
              4 + 3 = 7    (第三层)
              7 + 3 = 10   (第二层)
              10 + 3 = 13  (第一层)        最终返回结果给外部程序
    """

    if n == 1: return n                 # 符合递进终止条件
    return recursion(n - 1) + 3         # 最终返回结果给外部程序


count = 1
def recursion_debug(n: int, side=None, uid=None) -> int:
    """
    关键信息:
    递归函数, 会无线循环的递进,
    只需要一次跳出动作,
    递归函数, 将会开始层层回归, 直到回到递归函数的栈顶.
    """
    global count
    print(f"count: {count}; n: {n}; side: {side}; uid={str(uid).split('-')[0] if uid else uid}")
    count += 1
    if n == 1: return n                                                                                 # 符合递进终止条件
    s = n - 1
    result = recursion_debug(s, side="left", uid=uuid.uuid4()) + 3
    print(f"count: {count}; n: {n}; side: {side}; uid: {str(uid).split('-')[0]}; s: {s}; result: {result}")
    return result


def main():
    ss = recursion_debug(5)
    assert ss == 13


if __name__ == '__main__':
    main()

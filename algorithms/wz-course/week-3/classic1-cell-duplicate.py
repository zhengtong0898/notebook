from uuid import uuid4


class Solution:

    """
    经典案例-1 (细胞分裂)

    一个细胞的生命周期是3小时, 1小时分裂1次, 求n小时后, 容器内有多少净细胞?
    提示: 细胞会在每个小时的开始处先分裂后死亡.

    备注: 这不是一个 leetcode 的题目, 它是一个经典的递归算法题目.
    """

    def cell_duplicate(self, n: int):
        """
        params n: hours

        列出规律:
        第0个小时开始的时候,  1个细胞不分裂.                                                                  -- 累计死亡:  0
        第1个小时开始的时候,  1个细胞分裂成 2个细胞.                                                           -- 累计死亡:  0
        第2个小时开始的时候,  2个细胞分裂成 4个细胞.                                                           -- 累计死亡:  0
        第3个小时开始的时候,  4个细胞分裂成 8个细胞, 往前推4个小时的1个细胞开始死亡, 所以剩余7个净细胞.              -- 累计死亡:  1
        第4个小时开始的时候,  7个细胞分裂成14个细胞, 往前推4个小时的1个细胞开始死亡, 所以剩余13个净细胞.             -- 累计死亡:  2
                             关键问题: 这里往前推4个小时应该是2个细胞失望, 为啥之后1个细胞死亡?
                             关键回答: 因为第0个小时的细胞在第3小时的时候已经死亡, 所以第1小时只有1个细胞可死亡.
        第5个小时开始的时候, 13个细胞分裂成26个细胞, 往前推4个小时的2个细胞开始死亡, 所以剩余24个净细胞.             -- 累计死亡:  4
        第6个小时开始的时候, 24个细胞分裂成48个细胞, 往前推4个小时的4个细胞开始死亡, 所以剩余44个净细胞.             -- 累计死亡:  8
        第7个小时开始的时候, 44个细胞分裂成88个细胞, 往前推4个小时的7个细胞开始死亡, 所以剩余81个净细胞.             -- 累计死亡: 15

        归纳总结:
        要解这道题, 需要从第0个小时开始计算和根据题目要求的规律递增到第n小时, 最终得出结果.
        递归的特点就是, 当你传入一个n时, 它会先帮你层层递进到第0个小时(即: n = 1),
        然后再层层回归的过程中实时的累计计算, 最终得出结果.

        参考: https://blog.titanwolf.in/a?ID=01750-b64eb8bd-e1c9-4613-bfce-f998637ab5c5
        """
        if n < 0: return 0
        if n == 0: return 1
        if n == 1: return 2
        if n == 2: return 4
        if n == 3: return 7
        return (2 * self.cell_duplicate(n - 1)) - self.cell_duplicate(n - 4)

    def __init__(self):
        # 增加可观测代码
        self.leftmost_init = True
        self.leftmost_leaf = {}

    def cell_duplicate_debug(self, n: int, side=None, uid=None) -> int:
        if side == "right":
            self.leftmost_init = False

        if self.leftmost_init:
            self.leftmost_leaf[uid] = 1

        if n < 0: return 0
        if n == 0: return 1
        if n == 1: return 2
        if n == 2: return 4
        if n == 3: return 7
        left = 2 * self.cell_duplicate_debug(n - 1, "left", uuid4())
        right = self.cell_duplicate_debug(n - 4, "right", uuid4())
        result = left - right
        if self.leftmost_init is False and side in ("left", None) and self.leftmost_leaf.get(uid):
            print(f"n = {n:>2}; {left:>3} - {right} = {result}")
        return result


def main():
    ss = Solution().cell_duplicate(7)
    print("result: ", ss)


if __name__ == '__main__':
    main()

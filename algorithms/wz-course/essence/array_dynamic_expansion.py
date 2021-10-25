

class MyArrayList:

    """
    数组动态扩容
    """

    def __init__(self):
        # 初始容量指标: 当达到该指标后, 以倍增的形式扩容,
        # 例如: 100, 200, 400, 800, 1600, 3200.
        self.capacity = 100

        # 创建一个 "定长" 数组, 这里必须要严丝合缝.
        self.data = [0] * self.capacity

        # 当前有效的可写入位置
        self.writable_index = 0

    def append(self, element):

        # 判断是否触发扩容动作.
        if self.writable_index == self.capacity:

            # 构建-1: 建立一个新的列表, 大小是当前列表的两倍.
            new_data = [0] * (self.capacity * 2)

            # 构建-2: 将数据写入(完整的搬运)到新的列表中.
            for i in range(self.capacity):
                new_data[i] = self.data[i]

            # 构建-3: 将 "扩容后" 的数组, 覆盖 "原先" 的数组.
            self.data = new_data

            # 更新元数据指标: 标记下一次扩容的触发条件.
            self.capacity *= 2

        # 执行添加动作: 将 "值" 以末端添加的形式写入到列表中.
        self.data[self.writable_index] = element
        # 更新元数据指标: 标记下一个可写入位置.
        self.writable_index += 1

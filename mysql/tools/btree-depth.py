import math


class BTreeDepth:

    def __init__(self, row_size=224):
        # InnoDB 页大小(单位: byte)
        self.page_size = 16 * 1024

        # 主键类型大小, 通常是int, 所以是4-byte.
        self.primary_key_size = 4

        # InnoDB每个指针占位6-byte.
        self.pointer_size = 6

        # 一行数据大小(单位: byte)
        # 估算出一行数据中所有字段值大小的总合.
        # 假设一张表有以下几个字段, 那么相加得到224-byte(当作每行数据大小)
        # `username`(18-byte), `age`(3-byte), `gender`(3-byte), `email`(50-byte), `address`(150-byte)
        self.row_size = row_size

    def leaf_page_maxrows(self):
        """ 一个叶子节点最大能存储多少行数据 """
        return int(self.page_size / self.row_size)

    def index_page_maxleaf(self):
        """ 一个索引页最大能存储多少个叶子节点指针 """
        return int(self.page_size / (self.primary_key_size + self.pointer_size))

    def index_page_maxrows(self):
        """ 一个索引页最大能存储多少行数据 """
        return self.index_page_maxleaf() * self.leaf_page_maxrows()

    def maxrows_by_depth(self, level=2):
        """ 根据BTree高度, 计算出最大能存储多少行数据 """
        return pow(self.index_page_maxleaf(), level-1) * self.leaf_page_maxrows()

    def get_depth(self, rows=3000000):
        """
        根据表中的数据, 计算出B+树的高度.
        算法: log2(N)/log2(M)

        TODO: 1. 获取一张表有多少个index_page.
              2. 获取一个index_page有多少个key.

        参考: https://cloud.tencent.com/developer/news/373193
             https://www.percona.com/blog/2009/04/28/the_depth_of_a_b_tree/
        """
        return math.log2(rows) / math.log2(self.index_page_maxleaf())


def main():
    btree_depth = BTreeDepth()
    print(btree_depth.index_page_maxleaf())
    print(btree_depth.maxrows_by_depth(level=3))
    print(btree_depth.get_depth(222303256))


if __name__ == '__main__':
    main()
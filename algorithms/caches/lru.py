# 参考资料-1: https://docs.python.org/3/library/functools.html
# 参考资料-2: https://www.geeksforgeeks.org/lru-cache-in-python-using-ordereddict/
from collections import OrderedDict


class LRUCache:

    """
    LRU: least recently used
    可以将LRU理解为是一个缓存池, 它只缓存最近使用的值.
    一个已缓存的值, 被命中的频率越高, 它驻留的时间就越久.
    一个已缓存的值, 被命中的频率越低, 它驻留的时间就越短.

    下面的算法:
    命中的缓存会被移动到右侧, 右侧代表最近使用过的缓存.
    不被命中的缓存会逐步左移, 左侧代表最近低频使用的缓存.
    """

    def __init__(self, maxsize: int):
        self.cache = OrderedDict()
        self.maxsize = maxsize

    def get(self, key: int) -> int:
        result = None
        if key in self.cache:
            self.cache.move_to_end(key)
            result = self.cache[key]
        return result

    def put(self, key: int, value: int) -> None:
        # 先向最右侧插入数据
        # 如果元素总数大于上限, 向最左侧删除一个元素.
        self.cache[key] = value
        self.cache.move_to_end(key)
        if len(self.cache) > self.maxsize:
            self.cache.popitem(last=False)

import random


# 5:37 - 5:40
# 5:51 - 6:51
# 耗时: 74分钟
class Node:

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.forward = []

    def __repr__(self):
        return f"<Node key='{self.key}' value='{self.value}' level='{self.level}' at {hex(id(self))}>"

    @property
    def level(self):
        return len(self.forward)


class SkipList:

    def __init__(self, p: float = 0.5, max_level: int = 16):
        self.head = Node(key="root", value=None)
        self.p = p
        self.level = 0
        self.max_level = max_level

    def __str__(self):
        return f"<SkipList level='{self.level}' at {hex(id(self))}>"

    def __iter__(self):
        node = self.head
        while node.level != 0:
            yield node.forward[0].key
            node = node.forward[0]

    def random_level(self):
        level = 1

        while True:
            if random.random() >= self.p:
                break

            if level >= self.max_level:
                break

            level += 1

        return level

    def _locate_node(self, key):
        node = self.head
        update_vector = []

        # 从最高层级链表开始查找匹配
        for i in reversed(range(self.level)):

            # 尝试右移去查找匹配
            while True:
                index_invalid = i >= len(node.forward)
                if index_invalid: break

                rightmost_node = node.forward[i]
                if rightmost_node.key >= key: break

                node = rightmost_node

            update_vector.append(node)

        update_vector.reverse()

        if node.level <= 0:
            return None, update_vector

        if node.forward[0].key != key:
            return None, update_vector

        return node.forward[0], update_vector

    def delete(self, key):
        node, update_vector = self._locate_node(key)

        if node is None:
            return None

        for i, update_node in enumerate(update_vector):
            index_invalid = i >= update_node.level
            if index_invalid: continue

            key_equal = update_node.forward[i].key == node.key
            if not key_equal: continue

            if i >= node.level:                                     # 已是最右节点
                update_node.forward = update_node.forward[:i]
            else:                                                   # 不是最右节点
                update_node.forward[i] = node.forward[i]

    def insert(self, key, value):
        node, update_vector = self._locate_node(key)

        if node is not None:
            node.value = value
            return node

        level = self.random_level()
        if level > self.level:
            for i in range(self.level, level):
                update_vector.append(self.head)
            self.level = level

        new_node = Node(key=key, value=value)
        for i, update_node in enumerate(update_vector):
            if i >= update_node.level:                              # 已是最右节点.
                update_node.forward.append(new_node)
            else:                                                   # 不是最右节点.
                the_next = update_node.forward[i]
                new_node.forward.append(the_next)
                update_node.forward[i] = new_node

    def find(self, key):
        node, _ = self._locate_node(key)
        if node is not None:
            return node.value


def test_insert():
    skip_list = SkipList()
    skip_list.insert("Key1", 3)
    skip_list.insert("Key2", 12)
    skip_list.insert("Key3", 41)
    skip_list.insert("Key4", -19)

    node = skip_list.head
    all_values = {}
    while node.level != 0:
        node = node.forward[0]
        all_values[node.key] = node.value

    assert len(all_values) == 4
    assert all_values["Key1"] == 3
    assert all_values["Key2"] == 12
    assert all_values["Key3"] == 41
    assert all_values["Key4"] == -19


def test_insert_overrides_existing_value():
    skip_list = SkipList()
    skip_list.insert("Key1", 10)
    skip_list.insert("Key1", 12)

    skip_list.insert("Key5", 7)
    skip_list.insert("Key7", 10)
    skip_list.insert("Key10", 5)

    skip_list.insert("Key7", 7)
    skip_list.insert("Key5", 5)
    skip_list.insert("Key10", 10)

    node = skip_list.head
    all_values = {}
    while node.level != 0:
        node = node.forward[0]
        all_values[node.key] = node.value

    if len(all_values) != 4:
        print()
    assert len(all_values) == 4
    assert all_values["Key1"] == 12
    assert all_values["Key7"] == 7
    assert all_values["Key5"] == 5
    assert all_values["Key10"] == 10


def test_searching_empty_list_returns_none():
    skip_list = SkipList()
    assert skip_list.find("Some key") is None


def test_search():
    skip_list = SkipList()

    skip_list.insert("Key2", 20)
    assert skip_list.find("Key2") == 20

    skip_list.insert("Some Key", 10)
    skip_list.insert("Key2", 8)
    skip_list.insert("V", 13)

    assert skip_list.find("Y") is None
    assert skip_list.find("Key2") == 8
    assert skip_list.find("Some Key") == 10
    assert skip_list.find("V") == 13


def test_deleting_item_from_empty_list_do_nothing():
    skip_list = SkipList()
    skip_list.delete("Some key")

    assert len(skip_list.head.forward) == 0


def test_deleted_items_are_not_founded_by_find_method():
    skip_list = SkipList()

    skip_list.insert("Key1", 12)
    skip_list.insert("V", 13)
    skip_list.insert("X", 14)
    skip_list.insert("Key2", 15)

    skip_list.delete("V")
    skip_list.delete("Key2")

    assert skip_list.find("V") is None
    assert skip_list.find("Key2") is None


def test_delete_removes_only_given_key():
    skip_list = SkipList()

    skip_list.insert("Key1", 12)
    skip_list.insert("V", 13)
    skip_list.insert("X", 14)
    skip_list.insert("Key2", 15)

    skip_list.delete("V")
    assert skip_list.find("V") is None
    assert skip_list.find("X") == 14
    assert skip_list.find("Key1") == 12
    assert skip_list.find("Key2") == 15

    skip_list.delete("X")
    assert skip_list.find("V") is None
    assert skip_list.find("X") is None
    assert skip_list.find("Key1") == 12
    assert skip_list.find("Key2") == 15

    skip_list.delete("Key1")
    assert skip_list.find("V") is None
    assert skip_list.find("X") is None
    assert skip_list.find("Key1") is None
    assert skip_list.find("Key2") == 15

    skip_list.delete("Key2")
    assert skip_list.find("V") is None
    assert skip_list.find("X") is None
    assert skip_list.find("Key1") is None
    assert skip_list.find("Key2") is None


def test_delete_doesnt_leave_dead_nodes():
    skip_list = SkipList()

    skip_list.insert("Key1", 12)
    skip_list.insert("V", 13)
    skip_list.insert("X", 142)
    skip_list.insert("Key2", 15)

    skip_list.delete("X")

    def traverse_keys(node):
        yield node.key
        for forward_node in node.forward:
            yield from traverse_keys(forward_node)

    assert len(set(traverse_keys(skip_list.head))) == 4


def test_iter_always_yields_sorted_values():
    def is_sorted(lst):
        for item, next_item in zip(lst, lst[1:]):
            if next_item < item:
                return False
        return True

    skip_list = SkipList()
    for i in range(10):
        skip_list.insert(i, i)
    assert is_sorted(list(skip_list))
    skip_list.delete(5)
    skip_list.delete(8)
    skip_list.delete(2)
    assert is_sorted(list(skip_list))
    skip_list.insert(-12, -12)
    skip_list.insert(77, 77)
    assert is_sorted(list(skip_list))


def pytests():
    for i in range(100):
        # Repeat test 100 times due to the probabilistic nature of skip list
        # random values == random bugs
        test_insert()
        test_insert_overrides_existing_value()

        test_searching_empty_list_returns_none()
        test_search()

        test_deleting_item_from_empty_list_do_nothing()
        test_deleted_items_are_not_founded_by_find_method()
        test_delete_removes_only_given_key()
        test_delete_doesnt_leave_dead_nodes()

        test_iter_always_yields_sorted_values()


def main():
    pytests()
    skip_list = SkipList()
    skip_list.insert(1, "2")
    skip_list.insert(2, "2")
    skip_list.insert(3, "4")
    skip_list.insert(4, "4")
    skip_list.insert(5, "5")
    skip_list.insert(6, "4")
    skip_list.insert(7, "5")
    skip_list.insert(8, "4")

    print(skip_list)
    skip_list.insert(9, "4")

    key = input("find key: ")
    skip_list.delete(int(key))


if __name__ == '__main__':
    main()


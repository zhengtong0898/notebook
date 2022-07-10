from typing import Callable
from src.codes import snaggle

import pytest
from hypothesis import given, note, assume
from hypothesis.strategies import text, composite, SearchStrategy


# tdd
@pytest.mark.parametrize(
    "str_input,expect",
    [["abcdfeghi", True],
     ["goodboytitang", True],
     ["goodafternoon", True],
     ["helloworld", False]]
)
def test_snaggle_tdd(str_input: str, expect: bool) -> None:
    assert snaggle(str_input) == expect


# pbt
# property-base testing 不适合测试这种静态+分叉场景, 无法进行有意义的测试.
# 不太确定它是不是会成为一个失败用例.
@given(text())
def test_snaggle_pbt(ss: str) -> None:
    note(f"{ss}")
    assert snaggle(ss) == False      # 本身就是一对随即数据, 除了命中else分支,
                                     # 几乎不可能会命中其他条件分支, 因此这个测试用例毫无意义.


# pbt
# 如果硬是要用hypothesis测试这种场景, 那么就需要对数据进行约束(需要写一些代码来约束数据生成的方式).
class Node:
    def __init__(self, value: str):
        self.value = value
        self.next_node = None

    def set_next_node(self, next_node: "Node"):
        self.next_node = next_node


root_node = Node("")
node_a = Node("dfe")
node_b = Node("boyt")
node_c = Node("good")
node_d = Node("other")

root_node.set_next_node(node_a)
node_a.set_next_node(node_b)
node_b.set_next_node(node_c)
node_c.set_next_node(node_d)
node_d.set_next_node(node_a)


@composite
def custom_text(draw: Callable[[SearchStrategy[str]], str]):
    generated_value = draw(text())
    node: Node = root_node.next_node
    root_node.set_next_node(node.next_node)
    result = f"{generated_value}{node.value}"                   # 将数据约束在特定范式中.
    return result


@given(custom_text())
def test_snaggle_pbt_2(ss):
    expect = False if "other" in ss else True
    assert snaggle(ss) == expect


# 执行测试
# pytest -s --hypothesis-verbosity=debug

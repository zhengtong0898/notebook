from linear import StackLinear


def match_pairs(text):
    stack = StackLinear()

    valid_pairs, invalid_pairs = [], []

    for enum, i in enumerate(text):
        if i == "(":
            stack.append(enum)                              # 将所有左括号纳入栈中.
        elif i == ")":

            # 利用异常机制写法
            # try:
            #     top_item = stack.pop()
            # except Exception as e:
            #     invalid_pairs.append(enum)                # 左右括号配对失败(只有右括号没有左括号)
            # else:
            #     item = (top_item, enum)                   # 左右括号配对成功
            #     valid_pairs.append(item)

            # 无异常机制写法
            if stack.size() <= 0:
                invalid_pairs.append(enum)                  # 左右括号配对失败(只有右括号没有左括号)
            else:
                top_item = stack.pop()                      # 左右括号配对成功
                item = (top_item, enum)
                valid_pairs.append(item)

    for i in range(stack.size()):
        invalid_left_bracket = stack.pop()                  # 只有左括号, 没有右括号
        invalid_pairs.append(invalid_left_bracket)

    return valid_pairs, invalid_pairs


def test_1():
    text= "(a, b)"
    ss = match_pairs(text)
    assert ss == ([(0, 5), ], [])


def test_2():
    text = "(a, b()(()))"
    ss = match_pairs(text)
    assert ss == ([(5, 6), (8, 9), (7, 10), (0, 11)], [])


def test_3():
    text = "())"
    ss = match_pairs(text)
    assert ss == ([(0, 1)], [2, ])


def test_4():
    text = "((())"
    ss = match_pairs(text)
    assert ss == ([(2, 3), (1, 4)], [0, ])


def main():

    test_1()
    test_2()
    test_3()
    test_4()


if __name__ == '__main__':
    main()
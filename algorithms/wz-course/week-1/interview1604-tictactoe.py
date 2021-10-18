from typing import List


class Solution:

    """
    设计一个算法，判断玩家是否赢了井字游戏。输入是一个 N x N 的数组棋盘，由字符" "，"X"和"O"组成，其中字符" "代表一个空位。

    以下是井字游戏的规则：

    玩家轮流将字符放入空位（" "）中。
    第一个玩家总是放字符"O"，且第二个玩家总是放字符"X"。
    "X"和"O"只允许放置在空位中，不允许对已放有字符的位置进行填充。
    当有N个相同（且非空）的字符填充任何行、列或对角线时，游戏结束，对应该字符的玩家获胜。
    当所有位置非空时，也算为游戏结束。
    如果游戏结束，玩家不允许再放置字符。
    如果游戏存在获胜者，就返回该游戏的获胜者使用的字符（"X"或"O"）；
    如果游戏以平局结束，则返回 "Draw"；如果仍会有行动（游戏未结束），则返回 "Pending"。

    https://leetcode-cn.com/problems/tic-tac-toe-lcci/
    """

    def tictactoe(self, board: List[str]) -> str:
        assert isinstance(board, list)
        N = len(board)
        assert 0 < N == len(board[0])

        # 行
        for row in range(N):
            pieces = set(board[row])
            if len(pieces) == 1:
                answer = pieces.pop()
                if answer != " ":
                    return answer

        # 列
        # 遍历每一列, 采取反向遍历方式, 即: for col; for row;
        for col in range(N):
            pieces = set(board[row][col] for row in range(N))
            if len(pieces) == 1:
                answer = pieces.pop()
                if answer != " ":
                    return answer

        # 左对角
        pieces = set(board[row][row] for row in range(N))
        if len(pieces) == 1:
            answer = pieces.pop()
            if answer != " ":
                return answer

        # 右对角
        # 又对角的精华: (N-1) - row
        pieces = set(board[row][N-1-row] for row in range(N))
        if len(pieces) == 1:
            answer = pieces.pop()
            if answer != " ":
                return answer

        for row in board:
            if " " in row:
                return "Pending"

        return "Draw"


def test():
    solution = Solution()

    inputs = ["O X",
              " XO",
              "X O"]
    expect = "X"
    result = solution.tictactoe(board=inputs)
    assert result == expect

    inputs = ["OOX",
              "XXO",
              "OXO"]
    expect = "Draw"
    result = solution.tictactoe(board=inputs)
    assert result == expect

    inputs = ["OOX",
              "XXO",
              "OX "]
    expect = "Pending"
    result = solution.tictactoe(board=inputs)
    assert result == expect

    inputs = ["OX ",
              "OX ",
              "O  "]
    expect = "O"
    result = solution.tictactoe(board=inputs)
    assert result == expect

    inputs = ["O"]
    expect = "O"
    result = solution.tictactoe(board=inputs)
    assert result == expect

    inputs = [" O    X",
              " O     ",
              "     O ",
              "XXXXXXX",
              "  O    ",
              " O   O ",
              "O  X OO"]
    expect = "X"
    result = solution.tictactoe(board=inputs)
    assert result == expect

    inputs = ["   O",
              "X OX",
              " O  ",
              "O  X"]
    expect = "O"
    result = solution.tictactoe(board=inputs)
    assert result == expect

    inputs = ["OX    O ",
              "OX  X O ",
              "XX  O O ",
              "OX      ",
              " X      ",
              " X    O ",
              "XX      ",
              "OX  O O "]
    expect = "X"
    result = solution.tictactoe(board=inputs)
    assert result == expect

    inputs = ["   X O  O ",
              " X X    O ",
              "X  X    O ",
              "X    OX O ",
              "X   XO  O ",
              "X  X O  O ",
              "O  X O  O ",
              "     O  OX",
              "     O  O ",
              "   X XXXO "]
    expect = "O"
    result = solution.tictactoe(board=inputs)
    assert result == expect


def main():
    test()


if __name__ == '__main__':
    main()

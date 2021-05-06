

# 上三角矩阵(upper triangular matrix)
# 当 i>j 时, M(i, j) = '0'
def square_matrix():
    result = [['0'] * 9 for i in range(9)]

    for i in range(9):
        for j in range(9):
            if i <= j:
                result[i][j] = "x"

    return result


def main():
    ss = square_matrix()
    assert ss == [['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
                  ['0', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
                  ['0', '0', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
                  ['0', '0', '0', 'x', 'x', 'x', 'x', 'x', 'x'],
                  ['0', '0', '0', '0', 'x', 'x', 'x', 'x', 'x'],
                  ['0', '0', '0', '0', '0', 'x', 'x', 'x', 'x'],
                  ['0', '0', '0', '0', '0', '0', 'x', 'x', 'x'],
                  ['0', '0', '0', '0', '0', '0', '0', 'x', 'x'],
                  ['0', '0', '0', '0', '0', '0', '0', '0', 'x']]


if __name__ == '__main__':
    main()

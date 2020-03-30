# python3
from math import inf

def eval(a, b, op):
    if op == '+':
        return a+b
    elif op == '-':
        return a-b
    elif op == '*':
        return a*b
    else:
        assert False


def find_maximum_value(dataset):
    assert 1 <= len(dataset) <= 29
    d = dataset[::2]
    op = dataset[1::2]
    d = [int(i) for i in d]
    min_ = [[0] * (len(d) + 1) for _ in range(len(d) + 1)]
    Max = [[0] * (len(d) + 1) for _ in range(len(d) + 1)]
    for i in range(1, len(d) + 1):
        min_[i][i] = Max[i][i] = d[i - 1]
    n = len(d)
    for s in range(1, n):
        for i in range(1, n - s + 1):
            j = i + s
            mini, maxi = inf, -inf
            for k in range(i, j):
                a = eval(Max[i][k], Max[k + 1][j], op[k - 1])
                b = eval(Max[i][k], min_[k + 1][j], op[k - 1])
                c = eval(min_[i][k], Max[k + 1][j], op[k - 1])
                d = eval(min_[i][k], min_[k + 1][j], op[k - 1])
                mini = min(mini, a, b, c, d)
                maxi = max(maxi, a, b, c, d)
            min_[i][j] = mini
            Max[i][j] = maxi
    return Max[1][n]
    # type here


if __name__ == "__main__":
    print(find_maximum_value(input()))

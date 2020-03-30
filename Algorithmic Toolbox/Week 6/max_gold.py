# python3

from sys import stdin


def maximum_gold(capacity, weights):
    assert 1 <= capacity <= 10 ** 4
    assert 1 <= len(weights) <= 10 ** 3
    assert all(1 <= wi <= 10 ** 5 for wi in weights)

    '''max_ = [[0]*(len(capacity)+1) for _ in range(weights+1)]
    for i in range(len(capacity)):
        for j in range(weights+1):
            if i == 0 or capacity == 0:
                max_[i][j] = 0
            elif weights[i-1] <= capacity:
                max_[i][j] = max()'''
    value = [[0] * (len(weights) + 1) for _ in range(capacity + 1)]
    for i in range(1, len(weights) + 1):
        for j in range(1, capacity + 1):
            value[j][i] = value[j][i - 1]
            if weights[i - 1] <= j:
                val = value[j - weights[i - 1]][i - 1] + weights[i - 1]
                if val >= value[j][i]:
                    value[j][i] = val
    return value[capacity][len(weights)]

    # type here


if __name__ == '__main__':
    input_capacity, n, *input_weights = list(map(int, stdin.read().split()))
    assert len(input_weights) == n

    print(maximum_gold(input_capacity, input_weights))

# python3

from sys import stdin


def maximum_loot_value(storage, weights, values):
    value = 0
    max = 0
    pin = []
    index = 0
    while storage > 0:
        max = 0
        for i in range(len(weights)):
            if values[i] / weights[i] >= max and not (i in pin):
                max = values[i] / weights[i]
                index = i

        ic = min(weights[index], storage)
        storage -= ic

        value += ic * max
        pin.append(index)

    return value
    #type here


if __name__ == "__main__":
    data = list(map(int, stdin.read().split()))
    n, input_capacity = data[0:2]
    input_prices = data[2:(2 * n + 2):2]
    input_weights = data[3:(2 * n + 2):2]
    opt_value = maximum_loot_value(input_capacity, input_weights, input_prices)
    print("{:.10f}".format(opt_value))

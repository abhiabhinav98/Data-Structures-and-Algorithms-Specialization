# python3
import math

def linear_search(keys, query):
    for i in range(len(keys)):
        if keys[i] == query:
            return i

    return -1


def binary_search(keys, query):
    #assert all(keys[i] < keys[i + 1] for i in range(len(keys) - 1))
    #assert 1 <= len(keys) <= 3 * 10 ** 4

    minIndex = 0
    maxIndex = len(keys)-1

    while maxIndex >= minIndex:
        midIndex = math.floor((minIndex+maxIndex)/2)
        if keys[midIndex] == query:
            return midIndex
        elif keys[midIndex] < query:
            minIndex = midIndex + 1
        else:
            maxIndex = midIndex - 1
    return -1

    ##type here


if __name__ == '__main__':
    input_keys = list(map(int, input().split()))[1:]
    input_queries = list(map(int, input().split()))[1:]

    for q in input_queries:
        print(binary_search(input_keys, q), end=' ')

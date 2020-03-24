# python3
import math

def majority_element_naive(elements):
    assert len(elements) <= 10 ** 5
    for e in elements:
        if elements.count(e) > len(elements) / 2:
            return 1

    return 0


def majority_element(elements):
    assert len(elements) <= 10 ** 5
    mid = math.floor(len(elements)/2)
    count = {}

    for num in elements:
        if num in count:
            count[num] += 1
            if count[num] > mid:
                return 1
        else:
            count[num] = 1
    return 0

    #type here


if __name__ == '__main__':
    input_n = int(input())
    input_elements = list(map(int, input().split()))
    assert len(input_elements) == input_n
    print(majority_element(input_elements))

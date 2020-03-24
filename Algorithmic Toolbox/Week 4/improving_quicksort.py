# python3

from random import randint


def partition3(array, left, right):
    pivot = array[left]
    j = left
    k = right
    i = left

    while i <= right:
        if array[i] < pivot:
            array[j], array[i] = array[i], array[j]
            j += 1
            i += 1
        elif array[i] > pivot:
            array[i], array[right] = array[right], array[i]
            right -= 1
        else:
            i += 1

    return j, right
    #type here


def randomized_quick_sort(array, left, right):
    if left >= right:
        return
    pivot = randint(left, right)
    #pivot = array[(left + right)/2]

    array[left], array[pivot] = array[pivot], array[left]

    a,b = partition3(array, left, right)

    randomized_quick_sort(array, left, a - 1)
    randomized_quick_sort(array, b+1, right)
    #make a call to partition3 and then two recursive calls to randomized_quick_sort


if __name__ == '__main__':
    input_n = int(input())
    elements = list(map(int, input().split()))
    assert len(elements) == input_n
    randomized_quick_sort(elements, 0, len(elements) - 1)
    print(*elements)

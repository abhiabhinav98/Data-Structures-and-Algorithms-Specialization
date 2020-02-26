# python3


def largest_number_naive(numbers):

    largest = 0
    numbers.sort(reverse=True)
    for i in numbers:
        largest = largest*10**len(str(i)) + i

    return largest


def check(digit, max):
    return int(str(digit) + str(max)) >= int(str(max) + str(digit))


def largest_number(lst):
    largest = 0

    while lst != []:
        max = 0
        for digit in lst:
            if check(digit, max):
                max = digit
        largest = largest*10**len(str(max)) + max
        lst.remove(max)

    return largest

#type here


if __name__ == '__main__':
    n = int(input())
    input_numbers = list(map(int, input().split()))
    print(largest_number(input_numbers))

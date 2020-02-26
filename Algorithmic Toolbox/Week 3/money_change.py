# python3


def money_change(money):
    assert 0 <= money <= 10 ** 3
    a,b,c = 1,5,10
    sum = 0
    while money > 0:
        if money >= c:
            sum += money // c
            money %= c
        elif money >= b:
            sum += money // b
            money %= b
        else:
            sum += money // a
            break
    return sum

    #type here


if __name__ == '__main__':
    input_money = int(input())
    print(money_change(input_money))

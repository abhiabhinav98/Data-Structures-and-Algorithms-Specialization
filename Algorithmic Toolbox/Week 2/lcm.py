# python3

def gcd_fast(a, b):
    if b==0 :
        return a
    return gcd_fast(b, a%b)

def lcm_fast(a, b):
    return a//gcd_fast(a,b)*b

if __name__ == '__main__':
    a, b = map(int, input().split())
    print(lcm_fast(a, b))


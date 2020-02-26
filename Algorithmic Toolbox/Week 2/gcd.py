# python3

def gcd_fast(a, b):
    if b==0 :
        return a
    return gcd_fast(b, a%b)

if __name__ == "__main__":
    a, b = map(int, input().split())
    print(gcd_fast(a, b))
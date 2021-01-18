def gcd(a,b):
    return b if a==0 else gcd(b%a,a)


def solution(w,h):
    print(gcd(w,h))
    return w*h -(w+h) + gcd(w,h)


def main():
    print(solution(8,5))


main()


#단순 문자열 문제
#매 입력마다 데이터를 저장하는 것이 아니라
#값이 클 경우에만 저장

T = int(input())
for t in range(T):
    N = int(input())

    priceMax = 0
    who = ""
    for n in range(N):
        price, name = input().split()
        price = int(price)

        if price > priceMax:
            priceMax = price
            who = name

    print(who)

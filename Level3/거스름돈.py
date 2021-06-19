def solution(n, money):
    dp = [1] + [0] * n
    print(dp)
    for coin in money:
        for price in range(coin, n+1):
            print(coin, price)
            if price >= coin:
                dp[price] += dp[price - coin]

    print(dp)
    return dp[n] % 1000000007


def main():
    print(solution(5, [1, 2, 5]))


main()

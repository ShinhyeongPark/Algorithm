def gcd(a, b):
    while b != 0:
        r = a % b
        a = b
        b = r
    return a


def lcm(a, b):
    return int(a*b/gcd(a, b))


def solution(arr): #2,6,8,14
    arr = sorted(arr)
    arr_len = len(arr)

    step_lcm = lcm(arr[0], arr[1])

    for i in range(2, arr_len):
        step_lcm = lcm(step_lcm,arr[i])
        #print(step_lcm)

    return step_lcm
    # return arr


def main():
    print(solution([1,2,3]))


main()

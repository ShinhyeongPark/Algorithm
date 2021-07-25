import sys

T = int(input())

# answer = []
arr = set()
for _ in range(T):
    order = list(sys.stdin.readline().rstrip().split())
    # print(order)
    # num = int(num)
    if order[0] == "add":
        arr.add(int(order[1]))
    elif order[0] == "remove":
        arr.discard(int(order[1]))
    elif order[0] == "check":
        if int(order[1]) in arr:
            # answer.append(1)
            print("1")
        else:
            # answer.append(0)
            print("0")
    elif order[0] == "toggle":
        if int(order[1]) in arr:
            arr.remove(int(order[1]))
        else:
            arr.add(int(order[1]))
    elif order[0] == "all":
        arr.update([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11,
                   12, 13, 14, 15, 16, 17, 18, 19, 20])
    elif order[0] == "empty":
        arr = set()

# print(answer)

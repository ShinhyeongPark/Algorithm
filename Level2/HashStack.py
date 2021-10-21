n, p = map(int, input().split())

answer = 0
dicts = dict()


for _ in range(n):
    m, h = map(int, input().split())
    if m not in dicts:
        answer += 1
        dicts[m] = [h]
    else:
        while len(dicts[m]) > 0 and dicts[m][-1] > h:
            answer += 1
            dicts[m].pop()

        if dicts[m] == []:
            answer += 1
            dicts[m].append(h)
        else:
            if dicts[m][-1] < h:
                dicts[m].append(h)
                answer += 1

print(answer)

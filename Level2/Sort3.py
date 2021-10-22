def solution(citations):
    citations.sort(reverse=True)
    cSize = len(citations)  # 5
    # print(citations)
    for idx in range(cSize, -1, -1):
        count = 0
        for c in citations:
            if c >= idx:
                count += 1
            else:
                break

        if count >= idx and 5-count <= count:
            return idx

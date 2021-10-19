def solution(sizes):
    maxAns = 0

    rowA = 0
    rowB = 0

    default = 0  # 기준 열을 첫번째 열로
    # A열과 B열의 최대값을 구했다.
    for size in sizes:
        if size[0] > rowA:
            rowA = size[0]
        if size[1] > rowB:
            rowB = size[1]

    if rowB > rowA:
        default = 1  # B열의 최대값이 가장 클 경우, 기준 열을 두번쩨 열로
        maxAns = rowB
    else:
        maxAns = rowA

    # minAns = sizes[0][ans(default-1)]

    for i in range(len(sizes)):  # 행만큼 반복
        if sizes[i][default] == maxAns:
            continue

        if sizes[i][default] < sizes[i][abs(default-1)]:
            # print(i)
            sizes[i][default], sizes[i][abs(
                default-1)] = sizes[i][abs(default-1)], sizes[i][default]

    # print(sizes)
    minAns = 0
    for size in sizes:
        if size[abs(default-1)] > minAns:
            minAns = size[abs(default-1)]
    # print(minAns)
    return maxAns * minAns

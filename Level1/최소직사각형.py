def solution(sizes):
    maxAns = 0  # 기준 열의 최대값
    minAns = 0  # 기준이 아닌 열의 최대값

    rowA = 0  # First Row Max Value
    rowB = 0  # Second Row Max Value

    default = 0  # Standard Row (Start is First Row)

    # Calculate Max in First Row and Second Row
    for size in sizes:
        if size[0] > rowA:
            rowA = size[0]
        if size[1] > rowB:
            rowB = size[1]

    # if max in second row is bigger thab first row
    if rowB > rowA:
        default = 1  # standard row changes to second row
        maxAns = rowB  # max Values changes to max value of second row
    else:
        maxAns = rowA

    # loop for length of sizes
    for i in range(len(sizes)):
        if sizes[i][default] == maxAns:
            continue

        if sizes[i][default] < sizes[i][abs(default-1)]:
            sizes[i][default], sizes[i][abs(
                default-1)] = sizes[i][abs(default-1)], sizes[i][default]

    for size in sizes:
        if size[abs(default-1)] > minAns:
            minAns = size[abs(default-1)]

    return maxAns * minAns

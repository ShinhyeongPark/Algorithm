def solution(priorities, location):
    target = priorities[location] # 3 요청문서 우선순위 값
    index = [0] * len(priorities) # [0, 0, 0, 0]
    index[location] = 1 #동일한 숫자일 경우에 타겟 숫자일 경우 판별하기 위한 변수
    count = 0 #인쇄순서

    #[2,1,3,2]
    #[0,0,1,0]

    while 1:
        if priorities[0] == max(priorities) :
            if index[0] == 1:
                count += 1
                return count
            else:
                index.pop(0)
                priorities.pop(0)
                count += 1
        else:
            index.append(index.pop(0))
            priorities.append(priorities.pop(0))

    return count


def main():
    print(solution([1,1,9,1,1,1], 0))


main()
import heapq  # 힙 사용


def solution(jobs):
    last = -1  # 작업을 수행함에 따라 지금까지 작업이 이루어진 시간
    now = 0  # 현재 시간
    answer = 0  # 작업 총 소요 시간
    count = 0  # 작업의 수만큼 반복을 위한 변수
    n = len(jobs)  # 작업의 수
    wait = []  # 하나의 작업이 수행함에 있어, 기다리는 작업의 배열

    while (count < n):  # 작업만큼 반복
        for job in jobs:
            if last < job[0] <= now:  # 요청시간이 현재 시간보다 작을 때
                answer += (now - job[0])  # 현재시간과 요청시간의 차이
                heapq.heappush(wait, job[1])  # 대기열에 소요시간 저장
        if len(wait) > 0:  # 대기열에 작업이 존재할 경우
            answer += len(wait) * wait[0]  # 소요시간 * 대기열에 길이
            last = now  # last를 현재시간으로 갱신
            now += heapq.heappop(wait)  # 현재시간을 대기열에 소요시간을 더함
            count += 1
        else:  # 대기열에 작업이 없을 경우
            now += 1  # 현재시간 1씩 경과
    return answer // n

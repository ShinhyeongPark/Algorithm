def solution(id_list, report, k):
    # answer : user별 신고 메시지 수신 횟수
    answer = [0 for _ in range(len(id_list))]
    # 한 user가 중복으로 동일한 사용자를 신고하는 것 방지
    report = list(set(report))

    reportCount = dict()  # 각 user별 신고 당한 횟수
    reportList = dict()  # 각 User가 신고한 다른 User

    for id in id_list:
        reportCount[id] = 0
        reportList[id] = []

    for r in report:
        reporter = r.split()[0]
        reported = r.split()[1]

        reportCount[reported] += 1
        reportList[reporter].append(reported)

    banList = []
    for banUser in reportCount:
        if reportCount[banUser] >= k:
            banList.append(banUser)

    for i, receiveUser in enumerate(reportList):
        for ban in banList:
            if ban in reportList[receiveUser]:
                answer[i] += 1

    return answer

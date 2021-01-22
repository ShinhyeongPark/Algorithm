def solution(cacheSize, cities):
    cache = []
    answer = 0
    if cacheSize == 0:
        return len(cities) * 5

    for i in range(0, len(cities)):
        cities[i] = cities[i].lower()

    for v in cities:
        if len(cache) < cacheSize: #캐시가 아직 꽉 차지 않았을 경
            if v in cache: #캐시 hit
                cache.remove(v) #동일한 작업을 캐시에서 제거
                cache.append(v) #동일한 작업을 캐시의 마지막에 추가
                answer += 1 #실행시간 +1
            else: #캐시 miss
                cache.append(v) #캐시에 작업 추
                answer += 5 #실행시간 +5
        else: #캐시가 꽉 찼을 경우
            if v in cache: #캐시 hit
                cache.remove(v)
                cache.append(v)
                answer += 1
            else: #캐시 miss
                del cache[0] #캐시에 첫번째 원소: 가장 오랫동안 참조되지 않은 원소 삭제
                cache.append(v)
                answer += 5

    return answer


def main():
    print(solution(3, ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]))


main()
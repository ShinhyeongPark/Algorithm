import sys
from collections import defaultdict
# defaultdict: 딕셔너리의 초기값 타입 지정


def solution(genres, plays):
    answer = []  # 장르별 두개

    # {'classic': 1450, 'pop': 3100}
    genres_plays = defaultdict(int)
    # 'classic': [(0, 500), (2, 150), (3, 800)], 'pop': [(1, 600), (4, 2500)]}
    genres_songs = defaultdict(lambda: [])

    i = 0
    for g, p in zip(genres, plays):
        genres_plays[g] += p  # 장르별 총 재생수
        genres_songs[g].append((i, p))  # 장르당 (고유번호, 재생수)
        i += 1

    # [('pop', 3100), ('classic', 1450)]
    # 장르당 재생수 별로 정렬 = 재생수 총합이 큰 것 부터
    sorted_genres = sorted(genres_plays.items(),
                           key=(lambda x: x[1]), reverse=True)

    for g in sorted_genres:
        # 장르별로 각 노래 재생수로 정렬
        sorted_g = sorted(genres_songs[g[0]], key=lambda x: x[1], reverse=True)
        # 우선 한곡 추가
        answer.append(sorted_g[0][0])
        # 한곡 이상인 장르일 경우
        if len(sorted_g) > 1:
            answer.append(sorted_g[1][0])

    return answer


def main():
    print(solution([
        "classic", "pop", "classic", "classic", "pop"],
        [500, 600, 150, 800, 2500]
    ))


main()

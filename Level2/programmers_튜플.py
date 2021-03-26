def solution(s):
    ntuple = []
    #양끝에 괄호 제거
    s = s[2:-2]
    s = s.split("},{") #['2', '2,1', '2,1,3', '2,1,3,4']
    #사이즈 기준으로 정렬
    s.sort(key = len) #['2', '2,1', '1,2,3', '1,2,4,3']

    for tokens in s:
        token = tokens.split(",") #각 튜플을 ,로 분리하여 토큰 구함
        for to in token:
            if int(to) not in ntuple: #우리는 중복값을 허용하지 않는 튜플을 구하기때문에 리스트에 없을 경우
                ntuple.append(int(to)) #추가

    return ntuple

def main():
    print(solution("{{1,2,3},{2,1},{1,2,4,3},{2}}"))


main()

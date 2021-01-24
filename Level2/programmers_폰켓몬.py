def solution(nums):
    return min(int(len(nums)/2), len(list(set(nums))))
    
#nums의 사이즈의 절반과 nums의 중복을 제거했을 때 사이즈를 비교했을 때 작은 값이 가장 많이 가질 수 있는 종류이다.

def solution(people, limit):
    people.sort()
    c = 0
    i = 0
    j = len(people)-1
    
    while i<=j:
        c += 1
        if people[j] + people[i] <= limit:
            i += 1
        j -= 1
        
    return c
    
    #기존의 풀이로 알고리즘을 해결할 경우 효율성에서 통과하지 못한다.
    #이유는 리스트의 원소들을 비교하면서, 비교 후에 원소들을 삭제하는 연산에서 
    #추가적인 시간이 들기때문이다.
    #이를 해결하기 위해서는 원소들을 삭제할 필요없이
    #인덱스를 증가,감소시켜 삭제연산 없이 비교연산만으로 해결 가능하도록 했다.

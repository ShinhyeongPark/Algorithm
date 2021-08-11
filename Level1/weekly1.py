def solution(price, money, count):
    total = 0 # 총 이용료
    step = 1 # count만큼 반복하면서 N배를 계산하기 위한 변수
    
    while step != count+1:
        total += price * step
        step += 1
        
    if total < money: #돈이 부족하지 않을 경우
        return 0
    else: #돈이 부족하면 차액을 리턴
        return total - money
    

from math import gcd

def lcm(n,m): #최소공배수
    return n * m // gcd(n,m) #n과m의 곱을 최대공약수로 나눈 값

def solution(n, m):
    answer = []
    
    answer.append(gcd(n,m)) #최대공약수
    answer.append(lcm(n,m)) #최소공배수   
    
    return answer

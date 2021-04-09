w, h = input().split() 
#역순
w = list(w)
w.reverse()
h = list(h)
h.reverse()
#리스트 조인 후 정수 변환
w = int(''.join(w))
h = int(''.join(h))

print(max(w,h))


N = list(input())
#list 원소의 형변환 -> map(타입, 리스트)
number = list(map(int, N))
#역순정렬 // list.reverse()는 단순히 순서만 뒤집음
number.sort(reverse=True)
print(''.join(map(str,number)))

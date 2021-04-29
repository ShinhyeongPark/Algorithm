import heapq

def solution(operations):
    heap = []
    
    for op in operations:
        method, num = op.split(' ') #띄어쓰기 분리
        
        if method == "I": #Insert
            heapq.heappush(heap,int(num))
        elif heap: #heap이 비어있지 않은 상태 체크
            if num == "-1": #최소값 제거
                heapq.heappop(heap)
            else: #최대값 제거
                heap.remove(max(heap))

    return [0, 0] if not heap else [max(heap), min(heap)]

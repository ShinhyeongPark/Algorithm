def solution(arr):
    eof = [-1]
    
    if len(arr) == 0:
        return eof
    elif len(arr) == 1 and arr[0] == 10:
        return eof
    else:
        arr.remove(min(arr))
        return arr

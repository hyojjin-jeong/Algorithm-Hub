def solution(arr):
    c = len(arr)
    sum = 0
    for x in arr :
        sum = sum + x
    answer = sum / c
    return answer
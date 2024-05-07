def solution(n):
    answer = 0
    for x in range(1,n+1):
        if n % x == 0 :
            answer = answer + x
    return answer
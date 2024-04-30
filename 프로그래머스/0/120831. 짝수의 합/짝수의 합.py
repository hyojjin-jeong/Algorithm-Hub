def solution(n):
    num_list = [i for i in range(2, n+1, 2)]
    answer = sum(num_list)
    return answer
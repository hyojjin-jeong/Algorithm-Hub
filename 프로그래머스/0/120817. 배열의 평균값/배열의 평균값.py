def solution(numbers):
    answer = 0
    for x in numbers :
        answer = answer + x
    answer = answer / len(numbers)
    return answer
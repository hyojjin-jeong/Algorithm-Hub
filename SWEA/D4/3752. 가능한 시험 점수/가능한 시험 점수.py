from copy import deepcopy

T = int(input())
for t in range(T):
    N = int(input())
    scores = list(map(int,input().split()))
    answer = {0,scores[0]}
    for i in range(1,N):
        li = deepcopy(answer)
        for n in li:
            answer.add(n+scores[i])
    print(f'#{t+1} {len(answer)}')
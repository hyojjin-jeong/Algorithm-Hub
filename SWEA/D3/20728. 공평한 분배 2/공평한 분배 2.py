T = int(input())
for test_case in range(1, T + 1):
    N, K = map(int,input().split())
    candy = list(map(int,input().split()))
    candy.sort()
    answer = []
    if N == K:
        answer.append(candy[-1] - candy[0])
    else:
        for i in range(0,N-K+1):
            answer.append(candy[i + (K-1)] - candy[i])
    print(f'#{test_case} {min(answer)}')
import sys
input = sys.stdin.readline
import copy

N, M = map(int,input().split())

plus = [[0] * M]
for _ in range(N):
    li = list(map(int,input().split()))
    plus.append(li[1:])

# A 기업에 1~N만원을 투자했을 떄 최대 금액
# A,B 기업에 1 ~ N만원을 투자했을 때 최대 금액

dp = [[0] * (N+1) for _ in range(M)]
money = [[i] for i in range(N+1)]

for i in range(1,N+1):
    dp[0][i] = plus[i][0]

for i in range(1, M):
    first = copy.deepcopy(money)
    for j in range(N+1):
        li = 0
        second = []
        for k in range(j+1):
            if li < dp[i-1][k] + plus[j-k][i]:
                li = dp[i-1][k] + plus[j-k][i]
                second = first[k] + [j-k]
        dp[i][j] = li
        money[j] = second
print(dp[-1][-1])
print(*money[-1])
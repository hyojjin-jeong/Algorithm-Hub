def main():
    T = int(input())
    for t in range(T):
        N, L = map(int,input().split())
        food = []
        for _ in range(N):
            T, K = map(int,input().split())
            food.append([T,K])
        dp = [[0 for _ in range(L+1)] for _ in range(N+1)]
        for i in range(1,N+1):
            for j in range(L+1):
                T, K = food[i-1][0], food[i-1][1]
                if j >= K:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1], dp[i-1][j-K] + T)
                else:
                    dp[i][j] = dp[i-1][j]
        print(f'#{t+1} {dp[-1][-1]}')

if __name__ == "__main__":
    main()
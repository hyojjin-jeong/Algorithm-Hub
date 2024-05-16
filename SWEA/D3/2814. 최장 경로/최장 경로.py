
def back(x, cnt):
    global answer
    answer = max(answer, cnt)
    for next in graph[x]:
        if not visited[next]:
            visited[next] = True
            back(next, cnt+1)
            visited[next] = False


T = int(input())
for t in range(T):
    answer = 0
    N, M = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    for _ in range(M):
        x, y = map(int, input().split())
        graph[x].append(y)
        graph[y].append(x)
    for i in range(1, N+1):
        visited = [False for _ in range(N + 1)]
        visited[i] = True
        back(i, 1)
    print(f'#{t+1} {answer}')

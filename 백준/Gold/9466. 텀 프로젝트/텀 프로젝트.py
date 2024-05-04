import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

T = int(input())
def dfs(x):
    global answer
    next = graph[x]
    if not visited[next]:
        visited[next] = True
        li.append(next)
        dfs(next)
    else:
        if next in li:
            index = li.index(next)
            answer += li[index:]

for _ in range(T):
    n = int(input())
    li = list(map(int,input().split()))
    graph = [[] for _ in range(n+1)]
    for i in range(n):
        graph[i+1] = li[i]
    visited = [False] * (n+1)
    answer = []
    for i in range(1,n+1):
        if not visited[i]:
            visited[i] = True
            li = [i]
            dfs(i)
    print(n - len(answer))

import sys
input = sys.stdin.readline
from collections import deque  #큐 사용

K = int(input())
def bfs(i):
    q = deque()
    q.append(i)
    visited[i] = True
    group[i] = 1
    while q:
        x = q.popleft()
        for next in graph[x]:
            if not visited[next]:
                visited[next] = True
                group[next] = (-1) * group[x]
                q.append(next)
            else:
                if group[next] == group[x]:
                    return False
    return True
        
for _ in range(K):
    V, E = map(int,input().split())
    graph = {i : [] for i in range(1,V+1)}
    for _ in range(E):
        u, v = map(int,input().split())
        graph[u].append(v)
        graph[v].append(u)
    visited = [False] * (V+1)
    group = [0] * (V+1)
    result = "YES"
    for i in range(1,V+1):
        if not visited[i]:
            if not bfs(i):
                result = "NO"
                break
    print(result)
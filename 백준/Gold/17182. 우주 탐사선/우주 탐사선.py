import sys
input = sys.stdin.readline  # 필수로 해놓기
import heapq #다익스트라 알고리즘 사용

N, K = map(int,input().split())
INF = int(1e9)
maps = [list(map(int,input().split())) for _ in range(N)]

for k in range(N):
  for a in range(N):
    for b in range(N):
      maps[a][b] = min(maps[a][b], maps[a][k] + maps[k][b])

def back(start, cnt, time):
  global result
  if cnt == N:
    result = min(result, time)
    return
  for next in range(N):
    if not visited[next]:
      visited[next] = True
      back(next, cnt + 1, time + maps[start][next])
      visited[next] = False

visited = {i: False for i in range(N)}
result = INF
visited[K] = True
back(K,1,0)
print(result)
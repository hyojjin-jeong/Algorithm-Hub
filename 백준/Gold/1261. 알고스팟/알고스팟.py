import sys
input = sys.stdin.readline  #필수로 해놓기
import heapq #다익스트라 알고리즘 사용

M, N = map(int,input().split())
INF = float('inf')
graphs = [list(input().rstrip()) for _ in range(N)]
distance = [[INF] * M for _ in range(N)]
dx = [1,-1,0,0]
dy = [0,0,-1,1]
def dijkstra(x,y):
  q = []
  heapq.heappush(q, (0, x, y))
  distance[x][y] = 0
  while q:
    dist, X, Y = heapq.heappop(q)
    if dist > distance[X][Y]:
      continue
    for i in range(4):
      nx = X + dx[i]
      ny = Y + dy[i]
      if (0 <= nx < N) and (0 <= ny < M):
        if graphs[nx][ny] == "1" and dist + 1 < distance[nx][ny]:
          distance[nx][ny] = dist + 1
          heapq.heappush(q, (dist + 1, nx, ny))
        elif graphs[nx][ny] == "0" and dist < distance[nx][ny]:
          distance[nx][ny] = dist
          heapq.heappush(q, (dist, nx, ny))
dijkstra(0,0)
print(distance[-1][-1])
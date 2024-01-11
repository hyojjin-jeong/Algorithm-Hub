import sys
input = sys.stdin.readline  #필수로 해놓기
import heapq #다익스트라 알고리즘 사용

INF = float("inf")
def dijkstra(x,y):
  q = []
  heapq.heappush(q,(graphs[x][y],x,y))
  cost[x][y] = graphs[x][y]
  dx = [-1,1,0,0]
  dy = [0,0,-1,1]
  while q:
    c, a, b = heapq.heappop(q)
    if cost[a][b] < c:
      continue
    for i in range(4):
      nx = a + dx[i]
      ny = b + dy[i]
      if (0 <= nx < N) and (0 <= ny < N):
        cur_cost = graphs[nx][ny]
        if c + cur_cost < cost[nx][ny]:
          cost[nx][ny] = c + cur_cost
          heapq.heappush(q,(cost[nx][ny],nx,ny))
cnt = 1
while True:
  N = int(input())
  if N == 0:
    break
  graphs = [list(map(int,input().split())) for _ in range(N)]
  cost = [[INF] * N for _ in range(N)]
  dijkstra(0,0)
  print("Problem %d: %d"%(cnt,cost[-1][-1]))
  cnt += 1
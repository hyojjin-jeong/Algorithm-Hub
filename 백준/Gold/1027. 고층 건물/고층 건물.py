import sys
input = sys.stdin.readline  #필수로 해놓기

N = int(input())
builds = list(map(int,input().split()))
graphs = [[] for _ in range(N+1)]
for i in range(N):
  x1, y1 = i+1, builds[i]
  for j in range(i+1,N):
    x2, y2 = j+1, builds[j]
    a = (y2-y1) / (x2-x1)
    b = y2 - (a * x2)
    check = 0
    for k in range(i+1,j):
      x3, y3 = k+1, builds[k]
      if y3 >= (a * x3) + b:
        check += 1
    if check == 0:
      graphs[x1].append(x2)
      graphs[x2].append(x1)
ans = 0
for graph in graphs:
  if ans < len(graph):
    ans = len(graph)
print(ans)
  

import sys
input = sys.stdin.readline  #필수로 해놓기

N = int(input())
graphs = {}
for i in range(N):
  graphs[i] = ([],[])
nodes = list(map(int,input().split()))
for i in range(N):
  if nodes[i] != -1:
    graphs[nodes[i]][1].append(i)
    graphs[i][0].append(nodes[i])
    
R = int(input())
parent = graphs[R][0]
if len(parent) > 0:
  graphs[parent[0]][1].remove(R)
def remove_node(graphs, R):
  for j in graphs[R][1]:
    remove_node(graphs, j)
  del graphs[R]
remove_node(graphs, R)
ans = 0
for key, value in graphs.items():
  if len(value[1]) == 0:
    ans += 1
print(ans)
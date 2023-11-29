C = int(input())
I = int(input())

graph = [[] for _ in range(C+1)]

for _ in range(I):
    com1,com2 = map(int,input().split())
    graph[com1].append(com2)
    graph[com2].append(com1)

def dfs(graph,node,visited):
    if node not in visited:
        visited.append(node)
        for neighbor in graph[node]:
            dfs(graph,neighbor,visited)

visited = []
dfs(graph,1,visited)

print(len(visited)-1)
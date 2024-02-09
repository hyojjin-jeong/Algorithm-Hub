import sys
input = sys.stdin.readline
 
def find_parent(parent,x):
    if parent[x] != x :
        parent[x] = find_parent(parent,parent[x])
    return parent[x]
 
def union_parent(parent,x,y):
    x = find_parent(parent,x)
    y = find_parent(parent,y)
    if x < y:
        parent[y] = x
    else :
        parent[x] = y
 
n = int(input())
m = int(input())
enemy = [[] for i in range(n+1)]
parents = [i for i in range(n+1)]
 
for _ in range(m):
    relation,a,b = input().split()
    a,b = int(a),int(b)
    if relation == 'F':
        union_parent(parents,a,b)
    else :
        enemy[a].append(b)
        enemy[b].append(a)
 
for i in range(1,n+1):
    for e1 in range(len(enemy[i])):
        for e2 in range(e1+1,len(enemy[i])):
            union_parent(parents,enemy[i][e1],enemy[i][e2])
 
answer = set()
for i in range(1,n+1):
    answer.add(find_parent(parents,i))
 
print(len(answer))

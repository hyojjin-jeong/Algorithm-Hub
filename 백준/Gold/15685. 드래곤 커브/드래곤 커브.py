import sys
input = sys.stdin.readline

N = int(input())
use = []
location = {
    0: [1,0],
    1: [0,-1],
    2: [-1,0],
    3: [0,1]

}
for _ in range(N):
    x, y, d, g = map(int,input().split())
    dragon = [(x,y),(x + location[d][0], y + location[d][1])]
    d += 1
    if d == 4:
        d = 0
    loc = [d]
    last = 0
    for _ in range(g):
        reloc = loc[::-1]
        for l in reloc:
            nx = dragon[-1][0] + location[l][0]
            ny = dragon[-1][1] + location[l][1]
            dragon.append((nx,ny))
            l += 1
            if l == 4:
                l = 0
            loc.append(l)
    use.extend(dragon)
use = set(use)
answer = 0
for i in range(101):
    for j in range(101):
        square = {(i,j),(i+1,j),(i,j+1),(i+1,j+1)}
        if square.issubset(use):
            answer += 1
print(answer)
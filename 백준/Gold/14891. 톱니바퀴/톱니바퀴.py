import sys
input = sys.stdin.readline
from collections import deque

wheel = {
    1: deque(),
    2: deque(),
    3: deque(),
    4: deque()
}
for i in range(1,5):
    li = list(input().strip())
    for l in li:
        wheel[i].append(l)
K = int(input())

def left(num):
    change = []
    while num != 1:
        if wheel[num][6] != wheel[num-1][2]:
            change.append(num-1)
            num -= 1
        else:
            break
    return change



def right(num):
    change = []
    while num != 4:
        if wheel[num][2] != wheel[num+1][6]:
            change.append(num+1)
            num += 1
        else:
            break
    return change

def changeWheel(change,loc):
    for i in range(len(change)):
        if loc == 1:
            if i % 2 == 0: #반시계
                wheel[change[i]].append(wheel[change[i]].popleft()) 
            else: #시계
                wheel[change[i]].appendleft(wheel[change[i]].pop())
        else:
            if i % 2 == 0: #시계
                wheel[change[i]].appendleft(wheel[change[i]].pop())
            else: # 반시계
                wheel[change[i]].append(wheel[change[i]].popleft()) 

for _ in range(K):
    num, loc = map(int,input().split())
    lc = left(num)
    changeWheel(lc,loc)
    rc = right(num)
    changeWheel(rc,loc)
    if loc == 1:
        wheel[num].appendleft(wheel[num].pop()) # 시계
    else:
        wheel[num].append(wheel[num].popleft()) #반시계
answer = 0
for i in range(1,5):
    if wheel[i][0] == "1":
        answer += 2 ** (i-1)
print(answer)
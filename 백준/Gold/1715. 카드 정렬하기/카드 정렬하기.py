import sys
input = sys.stdin.readline
import heapq #다익스트라 알고리즘, 우선순위 큐 사용

N = int(input())
q = []
for _ in range(N):
    num = int(input())
    heapq.heappush(q, num)

answer = 0
while len(q) > 1:
    one = heapq.heappop(q)
    two = heapq.heappop(q)
    answer += one + two
    heapq.heappush(q, one + two)

print(answer)
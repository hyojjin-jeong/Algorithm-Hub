import sys
input = sys.stdin.readline

M, N = map(int,input().split())
nums = [False,False] + [True] * (N-1)
primes = []
for i in range(2, N+1):
  if nums[i]:
    primes.append(i)
    for j in range(2*i,N+1,i):
      nums[j] = False

for p in primes:
  if M <= p <= N:
    print(p)
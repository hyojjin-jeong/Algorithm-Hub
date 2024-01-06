import sys
input = sys.stdin.readline  #필수로 해놓기
sys.setrecursionlimit(10**7) #재귀함수 사용 시 필요

A, B = map(int,input().split())
oneSum = [0 for _ in range(60)]
for i in range(1,60):
  oneSum[i] = 2 ** (i-1) + 2 * oneSum[i-1]

def cnt(num):
  c = 0
  binNum = bin(num)[2:]
  length =  len(binNum)
  for i in range(length):
    if binNum[i] == '1':
      val = length - i - 1
      c += oneSum[val]
      c += (num - 2 ** val + 1)
      num -= 2 ** val
  return c
print(cnt(B) - cnt(A-1))
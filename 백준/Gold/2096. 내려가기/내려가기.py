import sys
input = sys.stdin.readline

N = int(input())
s1, s2, s3 = map(int,input().split())
M1, M2, M3 = s1, s2, s3
m1, m2, m3 = s1, s2, s3
for _ in range(N-1):
  n1, n2, n3 = map(int,input().split())
  M1, M2, M3 = n1 + max(M1,M2), n2 + max(M1,M2,M3), n3 + max(M2,M3)
  m1, m2, m3 = n1 + min(m1,m2), n2 + min(m1,m2,m3), n3 + min(m2,m3)
print(max(M1,M2,M3), min(m1,m2,m3))
import sys
input = sys.stdin.readline  #필수로 해놓기

N, K = map(int,input().split())
countries = [list(map(int,input().split())) for _ in range(N)]
for c in countries:
  if c[0] == K:
    country = c
    break
countries = sorted(countries, key = lambda x : (-x[1],-x[2],-x[3]))
index = countries.index(country)
ans = index + 1
for i in range(index-1,-1,-1):
  if countries[index][1:4] == countries[i][1:4]:
    ans -= 1
  else:
    break
print(ans)
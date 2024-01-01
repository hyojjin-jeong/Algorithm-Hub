import sys
input = sys.stdin.readline  #필수로 해놓기

N = int(input())
pillars = [list(map(int,input().split())) for _ in range(N)]
pillars = sorted(pillars, key=lambda x : x[0])
xPillars = []
yPillars = []
for x,y in pillars:
  xPillars.append(x)
  yPillars.append(y)
Max = max(yPillars)
Maxindex = yPillars.index(Max)
MaxX = xPillars[Maxindex]
x = xPillars[0]
y = yPillars[0]
sum = 0
for i in range(Maxindex+1):
  if y < yPillars[i]:
    sum += (xPillars[i] - x) * y
    x = xPillars[i]
    y = yPillars[i]
sum += Max
while Maxindex < len(yPillars)-1:
  xPillars = xPillars[Maxindex+1:]
  yPillars = yPillars[Maxindex+1:]
  Max = max(yPillars)
  Maxindex = yPillars.index(Max)
  sum += (xPillars[Maxindex] - MaxX) * Max
  MaxX = xPillars[Maxindex]
print(sum)
  
  
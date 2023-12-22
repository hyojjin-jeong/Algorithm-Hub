import sys
input = sys.stdin.readline  #필수로 해놓기

p, m = map(int,input().split())
players = [list(input().split()) for _ in range(p)]
rooms =[[] for _ in range(p)]
for level, name in players:
  level = int(level)
  for room in rooms:
    if len(room) == 0:
      room.append([level,name])
      break
    elif (len(room) < m and (level-10 <= int(room[0][0]) <= level+10)):
      room.append([level,name])
      break

while rooms and len(rooms[0]) > 0:
  if len(rooms[0]) == m:
    print("Started!")
    rooms[0] = sorted(rooms[0], key = lambda x : x[1])
    for i in rooms[0]:
      print(*i)
    rooms.pop(0)
  else:
    print("Waiting!")
    rooms[0] = sorted(rooms[0], key = lambda x : x[1])
    for i in rooms[0]:
      print(*i)
    rooms.pop(0)
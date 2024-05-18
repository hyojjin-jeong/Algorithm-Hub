T = int(input())
dx = [0,0,-1,1]
dy = [1,-1,0,0]
def dfs(x,y,num):
    if len(num) == 7:
        answer.add(num)
        return
    else:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (0 <= nx < 4) and (0 <= ny < 4):
                dfs(nx,ny, num + board[nx][ny])
for t in range(T):
    board = [list(input().split(" ")) for _ in range(4)]
    answer = set()
    for i in range(4):
        for j in range(4):
            dfs(i,j,board[i][j])

    print(f'#{t+1} {len(answer)}')
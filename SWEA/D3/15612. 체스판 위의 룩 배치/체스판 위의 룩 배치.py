def main():
    T = int(input())
    for t in range(T):
        answer = "no"
        board = []
        line = []
        rookcnt = 0
        for _ in range(8):
            line = list(input())
            rookcnt += line.count('O')
            board.append(line)
        if rookcnt == 8:
            flag = True
            for i in range(8):
                lowcnt = 0
                calcnt = 0
                for j in range(8):
                    if board[i][j] == "O":
                        lowcnt += 1
                    if board[j][i] == "O":
                        calcnt += 1
                if lowcnt != 1:
                    flag = False
                    break
                if calcnt != 1:
                    flag = False
                    break
            if flag:
                answer = "yes"
        print(f'#{t+1} {answer}')

if __name__ == "__main__":
    main()
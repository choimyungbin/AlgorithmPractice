n, m = map(int, input().split(" "))
board = []
min_color = []
for _ in range(n):
    board.append(input())
cnt = 0
for start_row in range(n-7):
    for start_col in range(m-7):
        countW = 0
        countB = 0
        for row in range(start_row, start_row+8):
            for col in range(start_col, start_col+8):
                # 홀수번째 칸들(인덱스는 짝수임, 0,2,4,...번째)
                if (row + col)%2 == 0:
                    if board[row][col] != 'W': countW += 1
                    if board[row][col] != 'B': countB += 1
                # 짝수칸들
                else:
                    if board[row][col] != 'W': countB += 1
                    if board[row][col] != 'B': countW += 1
        min_color.append(min(countW, countB))

print(min(min_color))
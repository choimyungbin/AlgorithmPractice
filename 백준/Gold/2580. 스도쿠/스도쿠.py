def push():
    global leng
    for y in range(9):
        for x in range(9):
            if board[y][x] == 0:
                blanky.append(y)
                blankx.append(x)
    leng = len(blanky)


def backtrack(blankidx):
    hor_queue = []
    ver_queue = []
    box_queue = []
    # 끝낼조건
    if blankidx == len(blankx):
        for i in range(9):
            print(*board[i])
        exit()
    # 아닐경우
    else:
        ver = [k[blankx[blankidx]] for k in board]
        box = sum([k[blankx[blankidx] // 3 * 3:blankx[blankidx] // 3 * 3+3] for k in
                         board[(blanky[blankidx] // 3 * 3):(blanky[blankidx] // 3 * 3 + 3)]],[])
        for i in range(1, 10):
            if i not in board[blanky[blankidx]]:
                hor_queue.append(i)
            if i not in ver:
                ver_queue.append(i)
            if i not in box:
                box_queue.append(i)

        for i in range(1, 10):
            if i in hor_queue and i in ver_queue and i in box_queue:
                board[blanky[blankidx]][blankx[blankidx]] = i
                backtrack(blankidx + 1)
                board[blanky[blankidx]][blankx[blankidx]] = 0


board = []
blanky = []
blankx = []
leng = 0
for i in range(9):
    board.append(list(map(int, input().split())))

push()
backtrack(0)
def star(n, y, x, blank):
    # base case
    if n == 3 and blank == 0:
        for i in range(n):
            res[y + i][x] = '*'
            res[y][x + i] = '*'
            res[y + n - 1][x + i] = '*'
            res[y + i][x + n - 1] = '*'
    elif n == 3 and blank == 1:
        for i in range(n):
            res[y + i][x] = ' '
            res[y][x + i] = ' '
            res[y + n - 1][x + i] = ' '
            res[y + i][x + n - 1] = ' '
    else:
        for j in range(3):
            star(n // 3, y, x+j * (n // 3), blank)
        for j in range(3):
            star(n // 3, y+n // 3, x+0 * (n // 3), blank)
            star(n // 3, y+n // 3, x+1 * (n // 3), 1)
            star(n // 3, y+n // 3, x+2 * (n // 3), blank)
        for j in range(3):
            star(n // 3, y+2 * (n // 3), x+j * (n // 3), blank)


N = int(input())
res = [[' ' for _ in range(N)] for _ in range(N)]
star(N, 0, 0, 0)
for s in res:
    print(''.join(s))

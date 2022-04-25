N = int(input())
length = 4 * N - 3
res = [[' ' for _ in range(length)] for _ in range(length)]


def star(n, x, y):
    # base case
    if n == 1:
        res[y][x] = '*'
        return

    tlength = 4 * n - 3
    for i in range(tlength):
        res[y][x + i] = '*'
        res[y + i][x] = '*'
        res[y + tlength - 1][x + i] = '*'
        res[y + i][x + tlength - 1] = '*'
    star(n - 1, x + 2, y + 2)


star(N, 0, 0)
for s in res:
    print(''.join(s))

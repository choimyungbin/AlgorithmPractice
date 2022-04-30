def check(n, y, x):
    num = screen[y][x]
    cnt = 0
    for i in range(y, y + n):
        for j in range(x, x + n):
            if screen[i][j] == num:
                cnt += 1
    return num, cnt == n ** 2


def compress(n, y, x):
    global result
    color, same = check(n, y, x)
    if same:
        result = result + str(color)
    else:
        result += "("
        compress(n // 2, y, x)
        compress(n // 2, y, x + n // 2)
        compress(n // 2, y + n // 2, x)
        compress(n // 2, y + n // 2, x + n // 2)
        result += ")"


N = int(input())
screen = []
result = ""
for i in range(N):
    screen.append(list(map(int, input())))
compress(N, 0, 0)
print(result)

def quad(x, y, size):
    color, chk = check(x, y, size)
    if chk:
        count[color] += 1
        return
    else:
        quad(x, y, size // 2)
        quad(x + size // 2, y, size // 2)
        quad(x, y + size // 2, size // 2)
        quad(x + size // 2, y + size // 2, size // 2)


def check(x, y, size):
    color = paper[x][y]
    cnt = 0
    for i in range(x, x + size):
        for j in range(y, y + size):
            if paper[i][j] == color:
                cnt += 1
    return color, cnt == size ** 2


paper = []
count = [0, 0]

n = int(input())
for i in range(n):
    paper.append(list(map(int, input().split(" "))))
quad(0, 0, n)
print(str(count[0]) + '\n' + str(count[1]))

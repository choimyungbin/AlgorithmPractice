def check(n, y, x):
    num = paper[y][x]
    cnt = 0
    for i in range(y, y + n):
        for j in range(x, x + n):
            if paper[i][j] == num:
                cnt += 1
    return num, cnt == n ** 2


def cut_paper(n, y, x):
    # base case
    num, same = check(n, y, x)
    if same:
        if num == -1:
            numCount[0] += 1
        elif num == 0:
            numCount[1] += 1
        elif num == 1:
            numCount[2] += 1
    else:
        cut_paper(n // 3, y, x)
        cut_paper(n // 3, y, x + n // 3)
        cut_paper(n // 3, y, x + 2 * (n // 3))
        cut_paper(n // 3, y + n // 3, x)
        cut_paper(n // 3, y + n // 3, x + n // 3)
        cut_paper(n // 3, y + n // 3, x + 2 * (n // 3))
        cut_paper(n // 3, y + 2 * (n // 3), x)
        cut_paper(n // 3, y + 2 * (n // 3), x + n // 3)
        cut_paper(n // 3, y + 2 * (n // 3), x + 2 * (n // 3))


N = int(input())
numCount = [0, 0, 0]  # one, zero, m-one
paper = []
for i in range(N):
    paper.append(list(map(int, input().split())))

cut_paper(N, 0, 0)
for i in numCount:
    print(i, end=' ')

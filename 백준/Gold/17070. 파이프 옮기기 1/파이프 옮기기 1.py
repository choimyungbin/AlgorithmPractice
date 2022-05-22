def recursive(y, x, shape):
    global ans
    # if y >= n or x >= n:
    #     return
    if y == n-1 and x == n-1:
        ans += 1
        return
    if (shape == 0 or shape == 2) and x+1 < n and home[y][x + 1] == 0:
        recursive(y, x + 1, 0)
    if (shape == 1 or shape == 2) and y+1 < n and home[y + 1][x] == 0:
        recursive(y + 1, x, 1)
    if y+1 < n and x+1 < n and home[y + 1][x] == 0 and home[y][x + 1] == 0 and home[y + 1][x + 1] == 0:
        recursive(y + 1, x + 1, 2)


n = int(input())
home = []
for i in range(0, n):
    row = list(map(int, input().split()))
    home.append(row)

ans = 0
recursive(0, 1, 0)
print(ans)

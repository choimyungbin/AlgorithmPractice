r, c = map(int, input().split())
board = []
for _ in range(r):
    board.append(list(map(int, input().split())))

count = 0

# 방향
dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]
visit = [[-1]*c for _ in range(r)]
def dfs(x, y):
    global count
    val = board[x][y]
    # 종료 조건
    if x == r-1 and y == c-1:
        return 1
    if visit[x][y] == -1:
        visit[x][y] += 1
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < r and 0 <= ny < c:
                temp = board[nx][ny]
                if temp < val:    # 더 낮은 계단칸
                    visit[x][y] += dfs(nx, ny)
    return visit[x][y]


result = dfs(0,0)
print(result)
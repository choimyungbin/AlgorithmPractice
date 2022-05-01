def search(n, y, x):
    global cnt
    # base case
    if n == 2:
        for i in range(n):
            for j in range(n):
                if y+i == find[0] and x+j == find[1]:
                    print(cnt)
                    exit()
                cnt += 1
    else:
        if find[0]-y<n//2:
            if find[1]-x<n//2:
                search(n // 2, y, x)
            else:
                cnt += (n//2)**2
                search(n // 2, y, x + n // 2)
        else:
            if find[1]-x<n//2:
                cnt += (n//2)**2*2
                search(n // 2, y + n // 2, x)
            else:
                cnt += (n//2)**2*3
                search(n // 2, y + n // 2, x + n // 2)


find = [0, 0]
cnt = 0
N, find[0], find[1] = map(int, input().split())
search(2 ** N, 0, 0)

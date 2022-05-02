n, m = map(int, input().split())
stack = []
def backtrack(slength):
    if slength == m:
        print(' '.join(map(str,stack)))
        return
    for i in range(1, n+1):
        if i in stack:
            continue
        stack.append(i)
        backtrack(slength+1)
        stack.pop()

backtrack(0)
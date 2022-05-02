n, m = map(int, input().split())
stack = []
def backtrack(qlength):
    if qlength == m:
        print(' '.join(map(str,stack)))
        return
    else:
        for i in range(1, n+1):
            stack.append(i)
            backtrack(len(stack))
            stack.pop()

backtrack(0)
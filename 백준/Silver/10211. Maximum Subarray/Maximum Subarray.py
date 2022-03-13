calNum = int(input())
for _ in range(calNum):
    array = [0]
    temp = []
    dp = [0] * 1001
    n = int(input())
    temp = map(int, input().split(" "))
    array += temp
    maxNum = 0
    # <--------------- 나만의 알고리즘
    dp[1] = array[1]
    for i in range(2, n + 1):
        dp[i] = max(dp[i - 1] + array[i], array[i])
    maxNum = max(dp[1:n+1])
    # ------------------------------->
    print(maxNum)

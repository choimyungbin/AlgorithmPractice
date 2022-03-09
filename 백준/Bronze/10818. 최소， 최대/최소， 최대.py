n = int(input())
arr = list(map(int, input().split()))
maxNum = arr[0]
minNum = arr[0]
for num in arr:
    if num > maxNum:
        maxNum = num
    if num < minNum:
        minNum = num
print(f'{minNum} {maxNum}')
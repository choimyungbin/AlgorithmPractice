n = int(input())
arr = list(map(int, input().split()))
arr.sort()
print(f'{arr[0]} {arr[n-1]}')
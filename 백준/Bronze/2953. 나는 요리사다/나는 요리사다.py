arr = [list(map(int, input().split())) for _ in range(5)]
sum_arr=[0,0,0,0,0]
maxNum=0
idx=0
for i in range(len(arr)):
    num = sum(arr[i])
    sum_arr[i] = num
    if num>maxNum:
        maxNum=num
        idx=i+1
print(f'{idx} {maxNum}')

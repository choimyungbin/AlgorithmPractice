metal = list(input())
stack = 0
count = 0
for i in range(len(metal)):
    if metal[i] == '(':
        if metal[i+1] == '(':
            stack += 1
        else:
            count += stack
    elif metal[i] == ')':
        if metal[i-1] == ')':
            stack -= 1
            count += 1
        else:
            continue
print(count)
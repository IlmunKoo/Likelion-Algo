import sys

n, k = list(map(int, sys.stdin.readline().split()))

coins = [int(input()) for _ in range(n)]
num = 0
i = len(coins) - 1
while True:
    if coins[i] <= k:
        num += k // coins[i]
        if k % coins[i] == 0:
            break
        k = k % coins[i]
        i -= 1
    else:
        i -= 1
print(num)


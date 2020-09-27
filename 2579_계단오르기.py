import sys

n = int(sys.stdin.readline().strip())
stairs = [int(sys.stdin.readline().strip()) for _ in range(n)]
dp = [0]*(n+1)

for i in range(n):
    if i == 0:
        dp[i] = stairs[i]
    elif i == 1:
        dp[i] = stairs[i-1] + stairs[i]
    elif i == 2:
        dp[i] = max(stairs[i-1]+ stairs[i] ,stairs[i-2]+ stairs[i]) #stairs[i-2] + stairs[i-1] 제외했더니 맞았다. i=2일 경우 계단 마지막 반드시 밟아야 하므로!!
    else:
        dp[i] = max(dp[i-2] + stairs[i],dp[i-3] + stairs[i-1] +stairs[i] )

print(dp[i])
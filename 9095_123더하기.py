import sys
T = int(sys.stdin.readline())
test_case = [int(sys.stdin.readline()) for _ in range(T)]

def dp(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    else:
        b = dp(n-3) + dp(n-2) + dp(n-1)
        return b


sol_total =0
for i in test_case:
    print(dp(i))



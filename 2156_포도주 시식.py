import sys
#런타임 에러

N = int(sys.stdin.readline())
wine_list= list()
for _ in range(N):
    wine_list.append(int(sys.stdin.readline()))

def dp(n):
    if n == 1:
        return wine_list[0]
    elif n==2:
        return wine_list[0] + wine_list[1]
    elif n == 3:
        return max(wine_list[0]+ wine_list[1], wine_list[1] + wine_list[2], wine_list[0]+ wine_list[2])
    else:
        return max(dp(n-4) + wine_list[n-3]+ wine_list[n-1], dp(n-4)+ wine_list[n-2] + wine_list[n-1], dp(n-4) + wine_list[n-3] + wine_list[n-2])

a= dp(N)
print(a)
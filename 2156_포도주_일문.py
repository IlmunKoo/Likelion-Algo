import sys


N = int(sys.stdin.readline())
wine_list= list()
wine_list.append(0)
for _ in range(N):
    wine_list.append(int(sys.stdin.readline()))

sol_list = [0 for _ in range(N+1)]
for i in range(1,N+1):
    if i == 1:
        sol_list[1] = wine_list[1]
    elif i == 2:
        sol_list[2] =  wine_list[1] + wine_list[2]

    else: sol_list[i] = max(sol_list[i-3] + wine_list[i-1]+ wine_list[i], sol_list[i-2] + wine_list[i], sol_list[i-1])

print(sol_list[N])

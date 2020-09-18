import sys
# 예제는 맞았는데 틀렸다고 뜬다.

N = int(sys.stdin.readline())
wine_list= list()
for _ in range(N):
    wine_list.append(int(sys.stdin.readline()))

sol_list = [0 for _ in range(N+1)]

for n in range(1, N+1):
    if n == 1:
        sol_list[1] = wine_list[0]
    elif n==2:
        sol_list[2] = wine_list[0] + wine_list[1]
    elif n == 3:
        sol_list[3] =max(wine_list[0]+ wine_list[1], wine_list[1] + wine_list[2], wine_list[0]+ wine_list[2])
    else:
        sol_list[n] = max(sol_list[n-4] + wine_list[n-3]+ wine_list[n-1], sol_list[n-4] + wine_list[n-2] + wine_list[n-1], sol_list[n-4] + wine_list[n-3] + wine_list[n-2])
# X00/0X0/00X
# 맨 마지막에서 4번째까지 최대의 포도주가 있다고 가정
# 끝 세 포도주의 최대값의 조합을 모두 더하려는 시도
#계단 아이디어에 집착한 나머지 맨 마지막을 포함한 로직을 짜지 못했다.
print(sol_list[N])
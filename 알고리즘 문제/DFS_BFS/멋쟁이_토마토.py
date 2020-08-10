import sys
from _collections import deque

M, N = map(int, sys.stdin.readline().split())
tomatoes = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

queue = deque()
#시작점 찾기
for m in range(N):
    for n in range(M):
        if tomatoes[m][n] == 1:
            queue.append([m,n])


# 좌 우 위 아래
dx = [-1,1, 0, 0]
dy = [0, 0, -1, 1]

breaker = False

#bfs
while len(queue) > 0:
    i, j = queue.popleft()
    for m in range(4):
        x = i + dx[m]
        y = j + dy[m]
        if 0 <= x < N and 0 <= y < M : #주어진 배열 넘어가지 않게 체크
            if tomatoes[x][y] == 0 and tomatoes[x][y] != -1: # 익지 않은 토마토 있고(0), 토마토 존재하는 곳일 때(-1)
                tomatoes[x][y] = tomatoes[i][j] + 1
                queue.append([x,y])


isNotRipe = False
result = 0

# for문 돌면서 안 익은 토마토(0) 있는지 확인
for i in tomatoes:
    result = max(result, max(i))
    if 0 in i:
        isNotRipe = True
if isNotRipe == True:
    print(-1)
else: #이미 다 익은 경우 while문에서 시작점만 체크하고 나오게 되어 있음, 어느곳도 가지 못한 경우 자연스레 1이 남기 때문에 따로 예외처리할 필요x
    print(result - 1)

    #원래는 시작점을 0으로 설정해야 하지만, 편의상 1로 설정했으므로 마지막에 빼준다.

# 막혔던 점
# 1. queue.pop(0)을 사용하면 O(N)이라서 deque.popleft()의 O(1)보다 느리다.
# 2. 예외처리 부분을 while문 안에서 했더니 시간초과가 뜸, 밖으로 꺼냈더니 ok
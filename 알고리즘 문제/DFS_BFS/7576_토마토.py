import sys

M, N = map(int, sys.stdin.readline().split())
tomatoes = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

ripe = [[0]*M for _ in range(N)]
queue = []
for m in range(N):
    for n in range(M):
        if tomatoes[m][n] == 1: #시작점 찾기
            ripe[m][n] = 1
            queue.append((m,n))
        elif tomatoes[m][n] == -1:  #-1도 ripe(visited)에 넣어줘야 -1(해를 구할 수 없을 때)와 구별 가능
            ripe[m][n] = -1

# 좌 우 위 아래
dx = [-1,1, 0, 0]
dy = [0, 0, -1, 1]

breaker = False

while len(queue) > 0:
    i, j = queue.pop(0)
    for m in range(4):
        x = i + dx[m]
        y = j + dy[m]
        if 0 <= x < N and 0 <= y < M : #주어진 배열 넘어가지 않게 체크
            if ripe[x][y] == 0 and tomatoes[x][y] != -1: # 익지 않은 토마토 있고(0), 토마토 존재하는 곳일 때(-1)
                ripe[x][y] = ripe[i][j] +1
                queue.append((x,y))

    if len(queue) == 0:
        for i in ripe:
            if 0 in i: # -1에 막혀 토마토 익지 못할 때
                print(-1)
                breaker = True  # 이중 for문 탈출
                break
        if breaker == True:
            break
        print(max(max(ripe)) -1)






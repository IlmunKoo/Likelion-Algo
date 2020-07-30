import sys

N = int(input())

location_list = []

#단지들을 이중리스트로 구현 &리스트 양 끝에 0 추가
for i in range(N):
    x = [int(x) for x in list(sys.stdin.readline().strip())]
    x.insert(0,0)
    x.append(0)
    location_list.append(x)


# 리스트 위와 아래도 0 추가
t  = [ 0 for _ in range(N+2)]
location_list.insert(0, t)
location_list.append(t)

# 탐색 위한 사전작업
# 1 [[0, 0, 0, 0, 0, 0, 0, 0, 0],
# 2 [0, 0, 1, 1, 0, 1, 0, 0, 0],
# 3 [0, 0, 1, 1, 0, 1, 0, 1, 0],
# 4 [0, 1, 1, 1, 0, 1, 0, 1, 0],
# 5 [0, 0, 0, 0, 0, 1, 1, 1, 0],
# 6 [0, 0, 1, 0, 0, 0, 0, 0, 0],
# 7 [0, 0, 1, 1, 1, 1, 1, 0, 0],
# 8 [0, 0, 1, 1, 1, 0, 0, 0, 0],
# 9 [0, 0, 0, 0, 0, 0, 0, 0, 0]]

#방문 표시할 이중리스트 구현
#이중리스트 구현 원하므로 리스트 두개 준비(바깥, 안)
visit_list = list()
for i in range(N+2):
    x = list()
    for j in range(N+2):
        x.append(False) #가로 열 채우기, 굳이 j 사용하지 않아도 O
    visit_list.append(x) #채운 가로 열을 세로로 쌓기

div_cnt_list = list()
cnt = 1

# 전체 반복문 작성
def DFS_All(G):
    global cnt
    for i in range(N+1):
        for j in range(N+1):
            if G[i][j] == False and location_list[i][j] == 1:
                DFS(i,j)
                div_cnt_list.append(cnt)
                cnt = 1
def DFS(j, k):
    global cnt #함수 밖에 있는 변수를 안에서도 쓰고 싶을 때 global 사용
    visit_list[j][k] = True

    # 전후좌우 체크
    if location_list[j+1][k] == 1:
        if visit_list[j+1][k] == False:
            cnt += 1
            DFS(j+1, k)
    if location_list[j][k+1] == 1:
        if visit_list[j][k+1] == False:
            cnt += 1
            DFS(j, k+1)
    if location_list[j-1][k] == 1:
        if visit_list[j-1][k] == False:
            cnt += 1
            DFS(j-1, k)
    if location_list[j][k-1] == 1:
        if visit_list[j][k-1] == False:
            cnt += 1
            DFS(j, k-1)

# 총 단지수
# 각 단지 아파트 수
DFS_All(visit_list) #방문체크용 그래프 인자로 전달
print(len(div_cnt_list))
for i in sorted(div_cnt_list):
    print(i)
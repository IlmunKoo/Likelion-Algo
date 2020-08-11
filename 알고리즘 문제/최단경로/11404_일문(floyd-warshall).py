import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
INF = 9999999999

floyd_warshall = [[INF]*n for _ in range(n)]

# 초기화 함수
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    if floyd_warshall[a-1][b-1] > c: #여러 개 노선중 weight가 더 작은 값 선택(INF일 때도 처리 가능)
        floyd_warshall[a-1][b-1] = c

 #relax
for k in range(n): #k는 거쳐가는 노드
    for i in range(n):
        for j in range(n):
            if floyd_warshall[i][j] > floyd_warshall[i][k] + floyd_warshall[k][j] and i != j:   # 자신으로 가는 정류장은 없으므로
                floyd_warshall[i][j] = floyd_warshall[i][k] + floyd_warshall[k][j]
            # if i == j: # INF를 0으로 바꿔줌
            #     floyd_warshall[i][j] = 0

for i in floyd_warshall:
    for j in i:
        if j == INF:
            print(0, end=" ")
        else:
          print(j, end=" ")
    print()



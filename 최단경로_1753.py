import sys
from heapq import heappop, heappush

v, e = map(int, sys.stdin.readline().split())
k = int(sys.stdin.readline())

INF = 100000000
route_table = [[] for _ in range(v+1)] #그래프
weight_table = [INF]*(v+1) #결과 저장
heap = []

# 다익스트라 기본조건: delMin과 decreaseKey
def daijk(start): #relax
    weight_table[start] = 0 # (가중치 테이블에서 시작 정점에 해당하는 가중치는 0으로 초기화해준다.)
    heappush(heap, [0 ,start]) # 거리를 앞에 두어 우선순위 큐에 넣을 때 거리가 비교되도록 한다

    while heap: # heap에 원소가 없을 때까지 반복
        weight, now = heappop(heap)   # delMin, 현재정점까지 가중치: weight, 현재에서 다음정점까지 가중치: w

        for  w, next_node  in route_table[now]: #연결된 노드 탐색
            next_weight = weight + w #이전거리와 현재 연결된 노드의 거리를 더해
            if next_weight < weight_table[next_node]: # 다음노드까지 가중치가 현재 기록된 값보다 작으면
                weight_table[next_node] = next_weight #relax 거리 갱신
                heappush(heap, [next_weight , next_node]) #우선순위 큐에 넣어준다.

for _ in range(e): #간선을 받아 그래프에 저장
    u, v, w = map(int, sys.stdin.readline().split())
    route_table[u].append([w,v])

daijk(k)

# 배열이 밑으로 계속 늘어나는 현상
for i in weight_table[1:]:
    print(i if i != INF else "INF")
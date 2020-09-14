import sys
from heapq import heappush, heappop
# heapify: 리스트를 힙으로 변환
inf = 100000000
v, e = map(int, sys.stdin.readline().split())
k = int(sys.stdin.readline())
s = [[] for _ in range(v + 1)]
route_matrix = [inf] * (v + 1)
heap = []

def dijkstra(start):
    route_matrix[start] = 0
    heappush(heap, [0, start])
    print(1, heap)
    while heap:
        w, n = heappop(heap)
        print(2, heap)
        for n_n, cost in s[n]:
            print(4, s[n])
            n_w = cost + w
            if n_w < route_matrix[n_n]:
                route_matrix[n_n] = n_w #relax
                heappush(heap, [n_w, n_n]) #decreaseKey(heap 성질을 만족하는 위치로 재배치) -> 다음으로 deleteMin 되는 노드는 s에서 갈 수 있는  가장 짧은 거리의 인접노드
                print(3, heap)
# s = [[], [[2, 2], [3, 3]], [[3, 4], [4, 5]], [[4, 6]], [], [[1, 1]]]
# for n_n, wei in s[n]:
# n_n , wei는 2,2 3,3 순서대로 for문을 돈다

for i in range(e):
    u, v, w = map(int, sys.stdin.readline().split())
    s[u].append([v, w])
print(s)
dijkstra(k)

for i in route_matrix[1:]:
    print(i if i != inf else "INF")
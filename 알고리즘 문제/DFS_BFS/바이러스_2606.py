import sys
from _collections import defaultdict

N = int(input())
M = int(input())
connected_computer = [list(map(int, sys.stdin.readline().split() ))for _ in range(M)]
#이차원리스트로 받음

marked = dict()
marked = defaultdict(str) #딕셔너리 예외처리, 없는 키값을 찾아도 오류가 뜨지 않도록

def DFS(v):
    marked.update({v : "visited"})
    for i in connected_computer:
        print(i)
        if v in i: #정점 체크(가지 않은 정점 = 가지 않은 모서리이므로 방문해준다)
            if marked[i[1]] != "visited":
                DFS(i[1])
            elif marked[i[0]] != "visited":
                DFS(i[0])

DFS(1)
print(marked)
print(len(marked)-1)
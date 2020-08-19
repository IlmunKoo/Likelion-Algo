from heapq import heappop, heappush
import sys

INF = 99999999
input = sys.stdin.readline()
T = int(sys.stdin.readline())
graph=None
def dijkstra(start,n):
  result = [INF]*n
  result[start]=0
  que=list()
  heappush(que,(result[start],start))
  while que:
    result_v,v=heappop(que)
    for fu,fw in graph[v]:
      if result[fu]>result_v+fw:
        result[fu]=result_v+fw
        heappush(que,(result[fu],fu))
  return result

for _ in range(T):
  n,m,t=map(int,input().split())
  s,g,h=map(int,input().split())
  s-=1
  g-=1
  h-=1

  graph=[[] for _ in range(n)]

  for _ in range(m):
    a,b,d=map(int,input().split())
    graph[a-1].append((b-1,d))
    graph[b-1].append((a-1,d))

  d=[]
  for _ in range(t):
    temp = int(sys.stdin.readline())
    d.append(temp-1)
  d.sort()
  ds,dg,dh=dijkstra(s,n),dijkstra(g,n),dijkstra(h,n)

  for i in range(t):
      if min(ds[g]*2+(dg[h]*2-1)+dh[d[i]]*2,ds[h]*2+(dh[g]*2-1)+dg[d[i]]*2,ds[d[i]]*2)%2==1:
        print(d[i]+1,end=' ') 
  print()



from sys import stdin
read = stdin.readline
dic={}
for i in range(int(read())):
    dic[i+1] = set()
for j in range(int(read())):
    a, b = map(int,read().split())
    dic[a].add(b)
    dic[b].add(a)

print(dic)

def bfs(start, dic):
    queue = [start]
    while queue:
        for i in dic[queue.pop()]:
            print(visited)
            if i not in visited:
                visited.append(i)
                print(1,  visited)
                queue.append(i)
                print(2, queue)

visited = []
bfs(1, dic)
print(visited)
print(len(visited) -1)
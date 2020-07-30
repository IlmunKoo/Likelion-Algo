from _collections import defaultdict
import sys

N = int(input())
all_list = list()

for i in range(N):
    all_list.append(list(sys.stdin.readline().strip()))

# print(all_list)
location_list = list()

for i in range(N):
    for j in  range(N):
        if all_list[i][j] == '1':
            location_list.append((i,j))


# print(location_list)

temp_count = 0

def DFS(v):
    j, k = v
    # location_list.remove((j,k))

    global temp_count
    temp_count += 1
    # if all_list[j][k+1] == 1: 이런식으로 하면 인덱스 에러 발생
    if (j+1, k) in location_list: #에러 회피
        location_list.remove((j+1, k))
        DFS((j+1, k))

    if (j, k+1) in location_list:
        location_list.remove((j, k+1))
        DFS((j, k+1))

    if (j-1, k) in location_list:
        location_list.remove((j-1, k))
        DFS((j-1, k))

    if (j, k-1) in location_list:
        location_list.remove((j, k-1))
        DFS((j, k-1))
    else:
        return


fin_count = 0
fin_list = list()
count_list = list()

while len(location_list) > 0 :
    v = location_list.pop()
    DFS(v)
    count_list.append(temp_count)
    temp_count = 0
    fin_count += 1


print(fin_count)
for i in sorted(count_list):
    print(i)

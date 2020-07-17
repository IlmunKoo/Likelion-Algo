import sys
reserveList = [list(map(int, sys.stdin.readline().split())) for _ in range(int(input()))]
reserveList.sort(key= lambda x: (x[1], x[0]))
largest = [reserveList[0]]
i = 1
j = 0
while True:
    if largest[j][1] <= reserveList[i][0]:
            largest.append(reserveList[i])
            i += 1
            j += 1
    else:
        i += 1
        
    if i > len(reserveList) - 1:
        break
print(len(largest))

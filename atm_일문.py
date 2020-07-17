import sys
n = int(input())
atmlist = sorted(list(map(int, sys.stdin.readline().split())))
total = 0

for i in range(1,n+1):
    for j in range(i):
        total += atmlist[j]

print(total)
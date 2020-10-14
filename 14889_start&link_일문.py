import itertools
import sys
N = int(sys.stdin.readline().strip())
temp = list(range(n))
synergy = []

for i in range(n):
    synergy.append(list(map(int,sys.stdin.readline().strip().split())))

p = list(itertools.combinations(temp,n//2))
answer=[]
for team in p:
    start = list(team)
    link = list(set(temp)-set(team))

    Synergy_start=0
    Synergy_link=0

    for i in start:
        for j in start:
            Synergy_start+=synergy[i][j]
    for i in link:
        for j in link:
            Synergy_link+=synergy[i][j]
    ans=abs(Synergy_link-Synergy_start)
    answer.append(ans)
print(min(answer))
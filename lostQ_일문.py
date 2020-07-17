# 50 - 60 + 45 - 40 + 70
splited  = input().split('-')
minus = []
for i in splited:
    total = 0
    m = i.split('+')
    for j in m:
        total += int(j)
    minus.append(total)
n = minus[0]
for i in range(1, len(minus)):
    n -= minus[i]
print(n)
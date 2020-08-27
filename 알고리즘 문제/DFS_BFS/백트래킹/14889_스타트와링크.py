import sys
from itertools import combinations
people = set()
stats = list()

N = int(sys.stdin.readline())
for i in range(N):
    people.add(i)
    stats.append(list(map(int, sys.stdin.readline().split())))
separated = list(combinations(people, N // 2))


for i in range(len(separated)):
    separated[i] = set(separated[i])

sol = list()

difference = list()

def start_link_subtract(start_team, link_team):
    start_combinations = list(combinations(list(start_team), 2))
    link_combinations = list(combinations( list(link_team), 2))

    start_val = 0
    link_val = 0

    for i ,j in start_combinations:
        start_val += stats[i][j] + stats[j][i]

    for i, j in link_combinations:
        link_val += stats[i][j] + stats[j][i]

    return abs(start_val-link_val)


diff_list = list()

while separated:
    start_team = separated.pop()
    link_team = people - start_team
    diff_list.append(start_link_subtract(start_team,link_team))

print(min(diff_list))

# 배운 것
# 1. combinations의 활용
# 조합은 기본적으로 순서만 바뀐 원소들의 중복을 제거한 상태이다.
# 순열은 순서가 바뀐 원소들도 다른 원소들로 인식한다.
# 2. set의 활용
# start와 link팀을 나누는 과정에서
# start팀을 조합으로 먼저 구한 후
# 전체(people)에서 start팀을 차집합의 개념으로 뺄 수 있다!!
# 3. for문 돌릴 때 range(N)이 같다면 같이 돌리는 것 고려!

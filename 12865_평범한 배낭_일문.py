import sys
from itertools import combinations

# 아이디어: 가능한 모든 item들의 조합의 index를 구해서 이것을 다 더한 것들 중 max를 찾아 return
# 처음에는 dp의 특징을 활용해 표를 그려 해를 찾으려고 했지만 순차적인 조합만을 커버할 수 있었고
# 임의의 조합은 커버할 수 없다는 문제점이 있었다.

N, K = list(map(int, sys.stdin.readline().split()))
x_list = [list(map(int, sys.stdin.readline().split())) for _ in range(N)] #w와v의 조합 input

N_list = [i for i in range(N)]
sol_list= list() # 모든 가능한 조합의 집합

for  i in range(1, N): #0부터 하면 공집합이 생기기 때문에 이를 처리하려면 1부터 설정
    N_combinations = [list(x)for x in combinations(N_list, i)]
    sol_list.extend(N_combinations)

fin_list = list()
w_sum = 0
v_sum = 0
while sol_list:
    temp = sol_list.pop()
    for i in temp: #인덱스를 실제 조합과 매칭
        w_sum += x_list[i][0]
        if w_sum  <= K :
            v_sum += x_list[i][1]
        else:
            w_sum -= x_list[i][0]

    fin_list.append((w_sum, v_sum))
    w_sum = 0
    v_sum = 0

a, b = max(fin_list)
print(b)
import sys

# 인터넷 참고
# 아이디어 : dp표를 1~k까지 무게를 기준으로 둘면서
# 현재 물건이 가방 속 물건보다 작다면 이전 값 그대로 가져온다
# 그렇지 않으면, (1)현재 물건을 넣어준 후, 남은 무게를 채울 수 있는 최댓값을 더해준다
# (2) 다른 물건들로 채워준다
# (1) 과 (2) 중 더 큰 값을 knapsack에 저장

n, k = map(int, sys.stdin.readline().split())
stuff =[[0, 0]]
for _ in range(n):
    stuff.append(list(map(int, sys.stdin.readline().split())))

knapsack = [[0]*(k+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, k+1):
        weight = stuff[i][0]
        value = stuff[i][1]

        if weight > j:
            knapsack[i][j] = knapsack[i-1][j]
        else:
            knapsack[i][j] = max(value+ knapsack[i-1][j-weight], knapsack[i-1][j])
        #이전 행 중에서 j-weight에 해당하는 열을 선택

print(knapsack[n][k])
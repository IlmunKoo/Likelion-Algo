import sys
N = int(sys.stdin.readline().strip())
sequence = list(map(int, sys.stdin.readline().split()))
sol_list = list()
len_list = list()
for i in range(N):
    sol_list.append(sequence[i])
    for j in range(N):
        if i >= j :
            continue
        else:
            if sequence[j] <= sol_list[len(sol_list)-1]:
                continue
            else:
                sol_list.append(sequence[j])
    len_list.append(len(sol_list))
    sol_list.clear()
print(max(len_list))

# 다음 반례를 풀지 못해 틀림
# 즉, 첫 1, 4,5를 잡아낸 후 다음 2 3 4 5를 잡아내지 못하는 문제점이 있었다.
# 7
# 1 4 5 2 3 4 5


# 점에서 차원이 갈라지거나
#
# 점화식이 간단하게 만들어지거나
#
# 점화식이 반복적으로 만들어지거나
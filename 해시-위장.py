from itertools import combinations
from collections import defaultdict

# 실패
def solution(clothes):
    answer = 0
    clothes_dict = dict()
    for clothe, clothes_type in clothes:
        if clothes_type in clothes_dict:
            clothes_dict[clothes_type] += 1
        else:
            clothes_dict[clothes_type] = 1

    temp_sum = 0
    temp_times = 1

    if len(clothes_dict.values()) < 2:
        temp_times = 0

    for value in clothes_dict.values(): # 1개 조합만 필요할 경우
        temp_sum += value
    for i in range(2, len(clothes_dict) + 1): # 2개 이상 조합이 필요할 경우
        temp_times += len(list(combinations(clothes_dict.keys(), i)))

    answer = temp_sum + temp_times
    return answer


# 통과
def solution(clothes):
    answer = {}
    for i in clothes:
        if i[1] in answer: answer[i[1]] += 1
        else: answer[i[1]] = 1

    cnt = 1
    for i in answer.values():
        cnt *= (i+1) # 입지 않는 경우까지 포함해서 곱해준다.
    return cnt - 1 # 적어도 한 가지 의상은 입어야 하므로 빼준다.
from math import ceil
from collections import deque
def solution(progresses, speeds):
# progresses, speeds, return
# [95, 90, 99, 99, 80, 99] [1, 1, 1, 1, 1, 1]	[1, 3, 2]

    answer = []
    days_required = deque()
		
		# 전처리 작업 
    for i in range(len(progresses)):
        val = (100 - progresses[i] )/ speeds[i] # 작업이 끝나는데 필요한 날짜(올림 이용)
        val = int(ceil(val))
        days_required.append(val)
        
    while days_required: #  [5, 10, 1, 1, 20, 1]
        temp = days_required.popleft()
        cnt = 1
        if len(days_required) == 0: #마지막 원소일경우 
            answer.append(1)
            break
            
        for i in range(len(days_required)): #[ 5 ,10, 1, 1, 20, 1]
            if days_required[i] > temp: # 뒤 프로그램 진도가 늦을 경우
                break
            cnt += 1

        answer.append(cnt)
        
        if cnt > 1:
            for _ in range(cnt-1): # 90, 99, 99 함께 완료되었을 경우 99, 99 큐에서 제거해주기
                days_required.popleft()

    return answer
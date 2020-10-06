from collections import deque
def solution(prices):
    answer = []
    prices = deque(prices)
    while prices:
        c = prices.popleft()

        count = 0
        for i in prices:
            if c > i:
                count += 1
                break # 감소하는 경우 1을 더하고 break -> 바로 append
            count += 1 #증가하거나 같을 경우 i을 더하고 for문을 계속 돈다

        answer.append(count)

    return answer




# deque이 아니라 queue를 써서 틀림
def solution(prices):
    answer = []
    cnt = 0
    while prices:
        a = prices.pop(0)
        if len(prices) == 0:
            answer.append(0)
            break
        for i in range(len(prices)):
            if a <= prices[i]:
                cnt += 1
                if i == len(prices)-1:
                    answer.append(cnt)
                    cnt = 0 #for문 위에 놔주면 각 초 간 초기화 효과가 있다.
                continue 
            else: # if문이 아니면 else가 실행되므로 굳이 안해도 된다
                cnt += 1
                answer.append(cnt) 
                cnt = 0
                break 
    return answer
def solution(bridge_length, weight, truck_weights):
    cnt = 0
    on_bridge = [0] * bridge_length 
    
    while on_bridge: # [0, 0]
        cnt += 1
        on_bridge.pop(0) #트럭 다리진입 시도
        if truck_weights: # [7,4,5,6]
            if sum(on_bridge) + truck_weights[0] <= weight: # 다리 위에 트럭이 올라갈 수 있는가
                on_bridge.append(truck_weights.pop(0)) # 트럭 정상진입
            else: # 다리가 견딜 수 없는 무게일 때
                on_bridge.append(0) # 트럭진입 x 표시 
    return cnt


from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    truck_weights = deque(truck_weights)
    on_bridge = deque()
    past_bridge = deque()
    total = 0 # 다리 위 무게 계산
    while truck_weights:#[7, 4, 5, 6]
        temp = truck_weights.popleft() 
        cnt = 0
        if len(on_bridge) <= bridge_length: # 다리 위에 있는 트럭이 다리 길이 이하일 때
                total += temp            
            if total <= weight: # 트럭 무게의 합이 다리가 견디는 weight보다 작거나 같을 때
                cnt += 1
                on_bride.append(temp)
            else:
                total -= temp
                truck_weights.appendleft(temp)
        else:
            answer.append(cnt)
            truck_past = on_bridge.popleft()
            past_bridge.append(truck_past)
            
    return answer
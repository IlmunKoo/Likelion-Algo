def solution(priorities, location):
    answer = 0
    while priorities:
        max_priority=max(priorities) # 가장 높은 우선순위
        current_printer=priorities.pop(0)  # 대기목록 맨 앞
        if max_priority==current_printer: 
            answer+=1 
            if location==0: # 내가 원하는 프린트물 위치
                break
            else:
                location -=1
        else:
            priorities.append(current_printer) # 맨뒤로
            if location==0: # 내가 원하는 프린트물 위치가 맨앞이었을 때
                location=len(priorities)-1 # 맨뒤로 
            else:
                location-=1
    return answer
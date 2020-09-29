import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville) #리스트의 heap화
    while True:
        a = heapq.heappop(scoville)  # heappop() 하는 순간 heap 내부에서 이진트리 재배치(새 최소값 발생)
        if a >= K:
            return answer
        else:
            if len(scoville) == 0:
                return -1
            b = heapq.heappop(scoville)
            new_sum = a + (2 * b)
            heapq.heappush(scoville, new_sum)
            answer += 1
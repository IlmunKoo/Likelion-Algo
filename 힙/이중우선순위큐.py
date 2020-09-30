import heapq


def solution(operations):
    answer = list()
    for e in operations:
        a, b = e.split()
        b = int(b)
        temp = list()
        if a == "I":
            heapq.heappush(answer, b)
        elif a == "D":
            if len(answer) == 0:
                continue
            else:
                if b == 1:
                    answer.pop()
                else:
                    for _ in range(len(answer)):
                        a = heapq.pop(answer)
                        temp.append(a)
                    temp[-1]

    if len(answer) == 0:
        return [0, 0]
    else:
        anwer
        most = answer.pop()
        least = answer.popleft()
        return [most, least]

    
def solution(brown, yellow):
    answer = []
    trivial = []
    subtraction = []
    minimun_sub = []
    total = yellow + brown
    for i in range(1, total + 1):
        if total % i == 0:
            trivial.append(total // i)
            
    if len(trivial) % 2 == 0:
        while trivial:
            a= trivial.pop()
            b= trivial.pop(0) 
            subtraction.append([a, b, abs(a-b)])
    else:
        while trivial:
            if len(trivial) == 1:
                x = trivial.pop()
                subtraction.append([x,x, 0])
                break
            a= trivial.pop()
            b= trivial.pop(0) 
            subtraction.append([a, b, abs(a-b)])
    minimun_sub = sorted(subtraction, key = lambda x : (x[2]))

    j, k, h = minimun_sub.pop(0)
    if j > k:
        answer.append(j)
        answer.append(k)
    else:
        answer.append(k)
        answer.append(j)
    return answer
import itertools 
def solution(numbers):
    answer = 0
    number = []
    result = []
    final= []
    for i in numbers:
        number.append(i)
        
    for i in range(1, len(numbers)+1):
        a =  list(map(''.join, itertools.permutations(number, i)))
        result.extend(a)
    
    judge = 0
    answer = 0        
    for i in range(len(result)):
        a = int(result.pop())
        final.append(a)
    final = set(final)
    final = list(final)

    while final:
        comparisonor = final.pop()
        if comparisonor == 1 or comparisonor == 0:
            continue
        for i in range(2, comparisonor):
            if comparisonor % i == 0:
                judge = 1
                break
        if judge == 0 :
            answer += 1
        judge = 0
            
            
    return answer
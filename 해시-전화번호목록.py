def solution(phone_book):
    answer = True
    breaker = False
    for i in phone_book:
        for j in phone_book:
            if i != j:
                if j.startswith(i):
                    answer = False
                    breaker = True
                    break
        if breaker == True:
            break
                    
        
    return answer
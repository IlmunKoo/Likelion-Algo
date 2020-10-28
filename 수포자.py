# 실패
def solution(answers):
    answer = []
    forgiver_1 = [1, 2, 3, 4,5 ]*(len(answer))
    forgiver_2 = [2,1, 2, 3, 2, 4, 2, 5]*(len(answer))
    forgiver_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]*(len(answer))
    score_1 = 0
    score_2 = 0
    score_3 = 0

    while answer:
        a= answer.pop()
        x= forgiver_1.pop()
        if a == x:
            score_1 += 1

        y= forgiver_2.pop()
        if a == y:
            score_2 += 1
            
        z= forgiver_3.pop()
        if a == z:
            score_3 += 1
    print(score_1, score_2, score_3)
    best_person = [score_1,score_2,score_3]
    max_score = max(best_person)
    for i in range(3):
        if best_person[i] == max_score:
            answer.append(i+1)
    
    return answer

# 프로그래머스 성공

2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
def solution(answers):
    pattern1 = [1,2,3,4,5]
    pattern2 = [2,1,2,3,2,4,2,5]
    pattern3 = [3,3,1,1,2,2,4,4,5,5]
    score = [0, 0, 0]
    result = []

    for idx, answer in enumerate(answers):
        if answer == pattern1[idx%len(pattern1)]:
            score[0] += 1
        if answer == pattern2[idx%len(pattern2)]:
            score[1] += 1
        if answer == pattern3[idx%len(pattern3)]:
            score[2] += 1

    for idx, s in enumerate(score):
        if s == max(score):
            result.append(idx+1)

    return result
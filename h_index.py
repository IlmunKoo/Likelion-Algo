def solution(citations):
    answer = 0
    n = len(citations)
    cnt = 0
    n_cnt = 0
    fin = []
    h_list = []
    for i in range(len(citations)):
        for j in range(len(citations)):
            if citations[i] >= citations[j]:
                cnt +=1
                
        if citations[i] >= cnt:
            h_list.append([cnt, citations[i]])
        cnt = 0
    fin = sorted(h_list, key= lambda x: -x[1])   
    print(fin)

    answer = fin[0][1]
    return answer
import sys

N, M = map(int, sys.stdin.readline().split())

number_list =[1+ i for i in range(N)]

check_number = [False]* N  #중복 체크
array = []

def DFS(x):
    if x == M:               #자리수 m을 충족하는지 체크
        print(0, *array)
        return

    for i in range(N):   #중복될 경우 패스
        if check_number[i]:
            continue

        array.append(number_list[i]) #수열 추가
        check_number[i] = True #사용한 수 체크
        DFS(x+1)
        array.pop()     #수열 마지막 자리 삭제
        check_number[i] = False  #사용한수 초기화

DFS(0)
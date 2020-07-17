client = [input().split() for _ in range(int(input()))] #리스트 표현식으로 2차원 배열 입력받기(입력받는 횟수먼저 입력해서 for문 몇번 돌지 초기화)
for i in client: i[0] = int(i[0])
client.sort(key = lambda x: x[0]) #람다 함수를 key변수에 담아줌, i[0]값으로 sorting
for i in client:
    print(" ".join(i))

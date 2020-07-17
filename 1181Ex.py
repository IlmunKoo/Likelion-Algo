wordList = [input() for _ in range(int(input()))] #리스트 표현식
noDuplicate = set(wordList) #중복제거
sorted = list(noDuplicate)
sorted.sort(key=lambda x: (len(x), x)) #람다식 사용한 정렬(1순위 길이, 2순위 사전)
for i in sorted:
    print(i)

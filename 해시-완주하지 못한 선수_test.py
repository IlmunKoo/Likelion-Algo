import sys

alphabet= "abcdefghijklmnopqrstuvwxyz"
sum = 0
string = list()
hash_participant = list()
hash_completion = list()

for char in participant: # 해시 출동 피하기 위해 항마다 고유한 계수 idx 부여
    sum += (alphabet.find(char)+1)**(2)*(31) # 알파벳 26개보다 큰 임의의 소수 31
    hash_participant.append(sum % 1234567891) # 임의의 소수
    sum = 0
hash_participant.sort()
for char in completion:
    sum += (alphabet.find(char)+1)**(2)*(31)
    hash_completion.append(sum % 1234567891)
    sum = 0
hash_completion.sort()


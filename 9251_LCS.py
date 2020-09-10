import sys

X = sys.stdin.readline().strip()
Y = sys.stdin.readline().strip()
x_list = list(X)
y_list = list(Y)

total_list = [[0]*len(y_list) for _ in range(len(x_list))]

for i in range(len(x_list)):
    for j in range(len(y_list)):
        if i > 0 and j > 0 :
            if x_list[i] == y_list[j]:
                total_list[i][j] = total_list[i-1][j-1] + 1
            else:
                total_list[i][j] = max(total_list[i-1][j], total_list[i][j-1])
print(total_list)
print(total_list[len(x_list)-1][len(y_list)-1]+ 1)
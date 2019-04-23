n = int(input())
int_list = list(map(int, input().split()))
count = 0
while True:
    isOdd = False
    for i in range(n):
        if(int_list[i] % 2 != 0):
            isOdd = True
    if isOdd:
        break
    for i in range(n):
        int_list[i] = int_list[i]/2
    count = count + 1
print(count)

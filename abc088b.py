# answer1 17ms 2940KB
n = int(input())
num_list = list(map(int, input().split()))

Alice = 0
Bob = 0

for i in range(n):
    current_max = max(num_list)
    if i % 2 == 0:
        Alice += current_max
    else:
        Bob += current_max
    num_list.remove(current_max)

print(Alice - Bob)


# answer2 18ms 2940KB
n = int(input())
num_list = list(map(int, input().split()))

Alice = 0
Bob = 0

num_list.sort(reverse=True)
for i, num in enumerate(num_list):
    if i % 2 == 0:
        Alice += num
    else:
        Bob += num

print(Alice - Bob)

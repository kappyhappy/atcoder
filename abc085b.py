# answer1
n = int(input())
num_list = [input() for i in range(n)]

bucket = {}
for i in range(1, 101):
    bucket[i] = 0
for i in range(n):
    bucket[int(num_list[i])] += 1
res = 0
for i in range(1, 101):
    if bucket[i] > 0:
        res += 1

print(res)

# answer2
n = int(input())
num_list = [input() for i in range(n)]

unique_num_dict = {}
for i in range(n):
    if num_list[i] in unique_num_dict.keys():
        unique_num_dict[num_list[i]] += 1
    else:
        unique_num_dict[num_list[i]] = 1

print(len(unique_num_dict))

# answer3
n = int(input())
num_list = [input() for i in range(n)]
unique_list = list(set(num_list))
print(len(unique_list))

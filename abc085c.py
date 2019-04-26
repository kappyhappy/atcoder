# answer1 LTE
n, y = map(int, input().split())

is_possible = False

for i in range(n+1):
    for j in range(n-i+1):
        for k in range(n-i-j+1):
            if (i + j + k) != n:
                continue
            total = i*10000 + j*5000 + k*1000
            if total == y:
                is_possible = True
                print("{} {} {}".format(i, j, k))
                break
        else:
            continue
        break
    else:
        continue
    break

if is_possible is False:
    print("-1 -1 -1")

# answer2 891ms 3060KB
n, y = map(int, input().split())

is_possible = False

for i in range(n+1):
    for j in range(n-i+1):
        k = n - i - j
        total = i*10000 + j*5000 + k*1000
        if total == y:
            is_possible = True
            print("{} {} {}".format(i, j, k))
            break
    if is_possible:
        break

if is_possible is False:
    print("-1 -1 -1")

# answer3 881ms 3060KB
n, y = map(int, input().split())

yukichi = -1
ichiyo = -1
hideyo = -1
for i in range(n+1):
    for j in range(n-i+1):
        k = n - i - j
        total = i*10000 + j*5000 + k*1000
        if total == y:
            yukichi = i
            ichiyo = j
            hideyo = k

print("{} {} {}".format(yukichi, ichiyo, hideyo))

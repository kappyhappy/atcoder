def calc_digit_sum(num):
    result = 0
    while num > 0:
        result += num % 10
        num //= 10
    return result

n, a, b = map(int, input().split())
result = 0
for i in range(1, n+1):
    digit_sum = calc_digit_sum(i)
    if digit_sum >= a and digit_sum <= b:
        result += i

print(result)


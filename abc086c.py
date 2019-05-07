n = int(input())
previous_t = 0
ans = "Yes"
for i in range(n):
    t, x, y = list(map(int, input().split()))
    if x + y > t:
        ans = "No"
        break
    if (x + y) % 2 != t % 2:
        ans = "No"
        break
    if previous_t > 0 and (abs(x - previous_x) + abs(y - previous_y) > (t - previous_t)):
        ans = "No"
        break
    previous_t = t
    previous_x = x
    previous_y = y

print(ans)


n = int(input())
# n = 3

print(n, end=" ")

while n != 1:
    if n % 2 == 0:
        n /= 2
    else:
        n *= 3
        n += 1
    print(int(n), end=" ")

print(int(n))

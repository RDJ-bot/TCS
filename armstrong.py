n = int(input())
ans = 0
m = n

while n > 0:
    rem = n % 10
    i = rem*rem*rem
    ans += i
    n = n//10

if m == ans:
    print("True")
else:
    print("False")
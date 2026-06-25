n = int(input())
toggled = ""

binary = bin(n)[2:]

for i in binary:
    if i == "1":
        toggled += "0"
    else:
        toggled += "1"

print(binary)
print(toggled)

answer = int(toggled,2)

print(answer)
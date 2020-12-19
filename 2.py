num1 = int(input())
num2 = int(input())
sum = 0

if 0 < num1 < 10:
    if num2 == num1:
        sum += 1
elif 9 < num1 < 100:
    if num2 == num1 // 10:
        sum += 1
    if num2 == num1 % 10:
        sum += 1
print(sum)

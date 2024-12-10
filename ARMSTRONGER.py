# creating the algorithm

num = int(input("Enter a number: "))
sum = 0 

temp = num 

while (temp > 0):
    digit = temp % 10
    digit = digit ** 3
    sum = sum + digit
    temp = temp // 10

if sum == num:
    print("The given number",num,"is a Armstrong number.")
else:
    print("The given number",num,"is not a Armstrong number.")
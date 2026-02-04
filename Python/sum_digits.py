sum = int(input("Enter a number: "))
total = 0
while sum > 0:
    digit = sum % 10
    total += digit
    sum = sum // 10
    print("Sum of digits:", total)
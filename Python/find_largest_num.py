numbers = [13, 7, 2, 9, 25]
largest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

print("The largest number is:", largest)
def sum_list(nums):
    total = 0
    for n in nums:
        total += n
    return total

#number = [1, 2, 3, 4, 5]

number = int(input("first number: "))
print("sum:", sum_list(range(1, number + 1)))
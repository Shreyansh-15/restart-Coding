def count_even(nums):
    count = 0
    for n in nums:
        if n % 2 == 0:
            count += 1
    return count

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("Even counts :", count_even(numbers))
def find_max(nums):
    maximum = nums[0]
    for n in nums:
        if n > maximum:
            maximum = n
    return maximum

numbers = [3, 7, 2, 9, 5]
print("Maximum:", find_max(numbers))
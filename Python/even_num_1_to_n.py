num = int(input("Enter a number: "))

print("Even numbers are: ")


for i in range(1, num + 1):
    if i % 2 == 0:
        print(i)

# # sum of even numbers from 1 to n
# num = int(input("Enter a number: "))
# total = 0

# for i in range(2, num+1, 2):
#     total += i

# print("Sum is:", total)
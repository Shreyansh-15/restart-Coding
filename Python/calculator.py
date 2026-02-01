a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

choice = input("Choose (+, -, *, /, %): ")

if choice == '+':
    print(a+b)
elif choice == '-':
    print(a-b)
elif choice == '*':
    print(a*b)
elif choice == '/':
    print(a/b)
elif choice == '%':
    print(a%b)
else:
    print("Invalid input")
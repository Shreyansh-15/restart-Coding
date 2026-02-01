age = int(input("Enter your age: "))

if age < 18:
    print("you are a minor.")

elif 18 <= age < 60:
    print("you are an adult.")

elif age >= 60:
    print("you are a senior citizen.")

else:
    print("Invalid age.")
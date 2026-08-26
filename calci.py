a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

def addition(a, b):
    return a + b

def multiplication(a, b):
    return a * b

print("1. Addition")
print("2. Multiplication")

choice = int(input("Enter choice: "))

if choice == 1:
    print(addition(a, b))
elif choice == 2:
    print(multiplication(a, b))
else:
    print("Wrong choice")
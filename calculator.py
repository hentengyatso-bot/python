# def add(x, y):
#     return x + y

# def subtract(x, y):
#     return x - y

# def multiply(x, y):
#     return x * y

# def divide(x, y):
#     if y == 0:
#         return "Error: Division by zero"
#     return x / y


# print("Select operation:")
# print("1. Add")
# print("2. Subtract")
# print("3. Multiply")
# print("4. Divide")
# print("5. Quit")

# while True:
#     choice = input("Enter choice (1/2/3/4/5): ")

#     if choice == '5':
#         print("Goodbye!")
#         break

#     if choice in ('1', '2', '3', '4'):
#         num1 = float(input("Enter first number: "))
#         num2 = float(input("Enter second number: "))

#         if choice == '1':
#             print(f"{num1} + {num2} = {add(num1, num2)}")
#         elif choice == '2':
#             print(f"{num1} - {num2} = {subtract(num1, num2)}")
#         elif choice == '3':
#             print(f"{num1} * {num2} = {multiply(num1, num2)}")
#         elif choice == '4':
#             print(f"{num1} / {num2} = {divide(num1, num2)}")
#     else:
#         print("Invalid choice. Please enter 1-5.")


def show(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} = {value}")

show(name="Henten", age=20)
# name = Henten
# age = 20
#Simple Calculator using match-case and dictionary

# def calculator():
#     a = int(input("Enter The First Number: "))
#     b = int(input("Enter The Second Number: "))

#     dict1 = {
#         "add": "+",
#         "sub": "-",
#         "mult": "*",
#         "div": "/",
#         "per": "%"
#     }

#     print("\nChoose operation:")
#     for key, value in dict1.items():
#         print(f"{key} ({value})")

#     operation = input("\nEnter operation (add, sub, mult, div, per): ").strip().lower()

#     match operation:
#         case "add":
#             print("The sum of a given no. is =", a + b)
#         case "sub":
#             print("The subtraction of a given no.is =", a - b)
#         case "mult":
#             print("The multiplication of a given no. is =", a * b)
#         case "div":
#             if b != 0:
#                 print("The div of a given no. is=", a / b)
#             else:
#                 print("Error: Division by zero")
#         case "per":
#             if b != 0:
#                 print("The per of a given no. is  =", a % b)
#             else:
#                 print("Error: Modulus by zero!")
#         case _:
#             print("Invalid operation!")
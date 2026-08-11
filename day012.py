#dict1 = {
#     "add": "+",
#     "sub": "-",
#     "mult": "*",
#     "div": "/",
#     "per": "%"
# }

# # Ask user which operation to perform
# operation = input("Enter operation (add, sub, mult, div, per): ").strip().lower()

# match operation:
#     case "add":
#         print(f"{a} {dict1['add']} {b} = {a + b}")
#     case "sub":
#         print(f"{a} {dict1['sub']} {b} = {a - b}")
#     case "mult":
#         print(f"{a} {dict1['mult']} {b} = {a * b}")
#     case "div":
#         if b != 0:
#             print(f"{a} {dict1['div']} {b} = {a / b}")
#         else:
#             print("Division by zero is not allowed!")
#     case "per":
#         if b != 0:
#             print(f"{a} {dict1['per']} {b} = {a % b}")
#         else:
#             print("Modulus by zero is not allowed!")
#     case _:
#         print("Invalid operation")
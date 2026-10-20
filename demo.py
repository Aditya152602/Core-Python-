# a=1
# b=2
# print("ADDITION OF TWO NO.",a+b)
# print("SUBTRACTION OF TWO NUMBERS",a-b)
# print("MULTIPLICATION OF A TWO NO. IS ",a*b)
# print("DIVISION OF TWO NUMBERS IS",a/b)
# print("PERCENTAGE OF A TWO NUMBERS IS",a%b)
# #DAY 9 TYPECASTING
# c="3"
# d="4"
# print(int(c)+int(d))
# string="15"
# number=8
# string_number = int(string)
# sum=number+string_number
# print("THE SUM OF BOTH THE NUMBERS IS: ", sum)
#DAY 10


# x=int(input("ENTER FIRST NO."))
# y=int(input("ENTER SECOND NUMBER"))
# print(x + y)

# print(int(x)+int(y))

#DAY16 MATCH CASE STATEMENT
# x=9
# match x:
#     case 0:
#         print("x is zero")
#     case 4:
#         print("case is 4")
#     case 5:
#         print("x is <10")
#     case _:
#         print(x) 
   
# DAY 17 FOR LOOPS

# name = 'Anushree'
# for i in name :
#     print(i)
#     if(i=="u"):
#         print("This is my life")

# colours =["red","blue","green","yellow"]
# for color in colours:
#     print(color)
#     for i in color:
#         print(i)
# for k in range(5):
#     print(k+1)
# for k in range(1,20001):
#     print(k)
# #for k in range(1,12,2):
  #  print(k)

#DAY 18 WHILE LOOPS IN PYTHON
# i=int(input("Enter the no."))
# print(i)
# while(i<=38):
#     i = int(input("Enter The No."))
#     print(i)
# print("Done With The Loop")

# count=5
# while(count>0):
#     print(count)
#     count=count-1
# else:
#     print("I'm inside else ")
      

# DAY 19 BREAK AND CONTINUE
# for i in range (1,50,1):
#     print(i,end=" ")
#     if(i==50):
#         break
# else:
#     print("Mississippi")
# print("Thank You")    
# for i in [2,3,4,5,6,7,8,0]:
#     if (i%2!=0):
#         continue
#     print(i)
#DAY 20 FUNCTION IN PYTHON
# def calculateGmean(a,b):
#     mean=(a*b)/(a+b)
#     print(mean)

# def isGreater(a,b):
#     if(a>b):
#         print("FIRST NO.IS GREATER")
#     else:
#         print("SECOND NO. IS GREATER OR EQUAL")

# def isLesser(a,b):
#     pass

# a=9
# b=8
# isGreater(a,b)
# calculateGmean(a,b)

#DAY20
# def name (fname,lname):
#     print("Hello",fname,lname)
# name ("Anushree","Dwivedi")

# #DAY21
# def name(fname,mname="Jhon",lname="Whatson"):
#     print("Hello,", fname,mname,lname)
# name("Amy")

# def name (fname,mname,lname):
#     print("Hello,",fname,mname,lname)
# name(mname="Peter",lname="Wesker",fname="Jode")

# def name(fname,mname,lname):
#     print("Hello,",fname,mname,lname)
# name("Peter","Quill")
# def name (**name):
#     print("Hello,",name["fname"],name["mname"],name["lname"])
#     name(mname="ADITYA",lname="ANUJ",fname="DWIVEDI")

# def name(fname,mname,lname):
#     return "Hello,"+ fname+"  "+mname+"  "+lname
# print(name("Aditya", "Dhar","Dwivedi"))

#DAY 22 LIST IN PYTHON
# lst1=[1,2,3,4]
# print(lst1)

# details=["Anushree",18,"Anuj",9.8]
# print(details)
# Animals=["c","d","b","m","h","p"]
# print(Animals[3:5])
# print(Animals[5:2])

# a=int(input("Enter The First Number:"))
# b=int(input("Enter The Second Number:" ))
# dict1 ={"add":"+",
#         "sub":"-",
#         "mult":"*",
#         "div":"/",
#         "per":"%"}
# match dict1:
#     case "add":
#         print("The sum of two numbers is:", a + b)
#     case "sub":
#         print("The subtraction of two numbers is:", a - b)
#     case "mult":
#         print("The multiplication of two numbers is:", a * b)
#     case "div":
#         print("The division of two numbers is:", a / b)
#     case "per":
#         print("The modulus of two numbers is:", a % b)
#     case _:
#         print("Invalid operation")

# a = int(input("Enter The First Number: "))
# b = int(input("Enter The Second Number: "))

# dict1 = {
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
         
        
# Simple Calculator using match-case and dictionary

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

# # Run the calculator
# calculator()
# Kaun Banega Crorepatti (KBC) Game in Python

# questions = [
#     {
#         "question": "Which is the national animal of India?",
#         "options": ["A. Lion", "B. Tiger", "C. Elephant", "D. Leopard"],
#         "answer": "B"
#     },
#     {
#         "question": "Who is known as the Father of the Nation (India)?",
#         "options": ["A. Jawaharlal Nehru", "B. Bhagat Singh", "C. Mahatma Gandhi", "D. Subhas Chandra Bose"],
#         "answer": "C"
#     },
#     {
#         "question": "Which planet is known as the Red Planet?",
#         "options": ["A. Earth", "B. Jupiter", "C. Venus", "D. Mars"],
#         "answer": "D"
#     },
#     {
#         "question": "What is the capital of India?",
#         "options": ["A. Mumbai", "B. New Delhi", "C. Kolkata", "D. Chennai"],
#         "answer": "B"
#     }
# ]

# prizes = [1000, 5000, 10000, 50000]  # prize money per question

# print("\n🎉 Welcome to Kaun Banega Crorepatti (KBC)! 🎉\n")
# winnings = 0

# for i, q in enumerate(questions):
#     print(f"Q{i+1}: {q['question']}")
#     for opt in q["options"]:
#         print(opt)

#     ans = input("Enter your answer (A/B/C/D): ").strip().upper()

#     if ans == q["answer"]:
#         winnings = prizes[i]
#         print(f"✅ Correct! You have won ₹{winnings}\n")
#     else:
#         print(f"❌ Wrong Answer! The correct answer was {q['answer']}")
#         break

# print(f"\n🎊 Game Over! You take home ₹{winnings}")

# import random

# # Questions for KBC
# questions = [
#     {
#         "question": "Which is the national animal of India?",
#         "options": ["A. Lion", "B. Tiger", "C. Elephant", "D. Leopard"],
#         "answer": "B"
#     },
#     {
#         "question": "Who is known as the Father of the Nation (India)?",
#         "options": ["A. Jawaharlal Nehru", "B. Bhagat Singh", "C. Mahatma Gandhi", "D. Subhas Chandra Bose"],
#         "answer": "C"
#     },
#     {
#         "question": "Which planet is known as the Red Planet?",
#         "options": ["A. Earth", "B. Jupiter", "C. Venus", "D. Mars"],
#         "answer": "D"
#     },
#     {
#         "question": "What is the capital of India?",
#         "options": ["A. Mumbai", "B. New Delhi", "C. Kolkata", "D. Chennai"],
#         "answer": "B"
#     }
# ]

# prizes = [1000, 5000, 10000, 50000]  # Prize money per question
# lifelines = {"50-50": True, "Audience Poll": True, "Phone-a-Friend": True}

# print("\n🎉 Welcome to Kaun Banega Crorepatti (KBC)! 🎉\n")
# winnings = 0

# for i, q in enumerate(questions):
#     print(f"\nQ{i+1}: {q['question']}")
#     for opt in q["options"]:
#         print(opt)

#     while True:
#         ans = input("\nEnter your answer (A/B/C/D) or type 'lifeline': ").strip().upper()

#         # Lifeline Handling
#         if ans == "LIFELINE":
#             print("\nAvailable Lifelines:")
#             for key, available in lifelines.items():
#                 if available:
#                     print(f"- {key}")
#             choice = input("Choose a lifeline: ").strip().title()

#             if choice == "50-50" and lifelines["50-50"]:
#                 lifelines["50-50"] = False
#                 # Keep correct answer + 1 random wrong answer
#                 correct = q["answer"]
#                 wrongs = [opt[0] for opt in q["options"] if opt[0] != correct]
#                 keep = random.choice(wrongs)
#                 print("\n50-50 Lifeline Applied! Remaining options:")
#                 for opt in q["options"]:
#                     if opt[0] in (correct, keep):
#                         print(opt)

#             elif choice == "Audience Poll" and lifelines["Audience Poll"]:
#                 lifelines["Audience Poll"] = False
#                 print("\n📊 Audience Poll Results:")
#                 percentages = {opt[0]: random.randint(5, 30) for opt in q["options"]}
#                 percentages[q["answer"]] = random.randint(50, 80)  # Higher chance correct
#                 for opt in q["options"]:
#                     print(f"{opt}: {percentages[opt[0]]}%")

#             elif choice == "Phone-A-Friend" and lifelines["Phone-a-Friend"]:
#                 lifelines["Phone-a-Friend"] = False
#                 print("\n📞 Phone-a-Friend Suggestion:")
#                 # Friend has 70% chance to suggest the correct answer
#                 if random.random() < 0.7:
#                     print(f"Your friend thinks the answer is {q['answer']}")
#                 else:
#                     print(f"Your friend thinks the answer is {random.choice(['A','B','C','D'])}")
#             else:
#                 print("❌ Lifeline not available or already used.")
#             continue

#         # Answer Checking
#         if ans == q["answer"]:
#             winnings = prizes[i]
#             print(f"✅ Correct! You have won ₹{winnings}\n")
#             break
#         else:
#             print(f"❌ Wrong Answer! The correct answer was {q['answer']}")
#             winnings = 0 if i < 1 else prizes[i-1]  # safe money till last correct
#             print(f"You take home ₹{winnings}")
#             exit()

# print(f"\n🎊 Congratulations! You won ₹{winnings}")

#DAY 31
# s={2,4,2,6}
# print(s)

# info={}
# print(type(info))

# ad=set()
# print(type(ad))

#DAY 32
# s1={1,2,4,5,6}
# s2={6,7,8}
# print(s1.union(s2))
# s1.update(s2)
# print(s1,s2)

#Day 33
# dic={
#     1:"aditya",
#     2:"anuj",
#     3:"g",
#     4:"f",
#     5:"d",

# }
# print(dic[2])

#day40
# a=400
# b=600
# print("A") if a>b else print("=") if a==b else print("B")
# c=9 if a>b else 0
# print(c)

#DAYS 41
# marks=[20,40,60,80,100]
# for index, mark  in enumerate(marks):
#     print(mark)
#     if (index==4):
#         print("aditya, awesome!")
# name=['Aditya','Anuj','Yuvraj']
# for index, name in enumerate(name,start=1):
#     print(index,name)

#Day44
# import math
# math.floor
class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
    def first_name(self):
        l = self.name.split(" ")
        return l[0]

e = Employee("Aditya Dwivedi",1000000)
print(e.first_name())  

# Program to find the longest substring without repeating characters.

# Take a string as input from the user.
text = input("Enter a string: ")

# Store the starting index of the current substring.
start = 0

# Store the maximum length found so far.
max_length = 0

# Create a dictionary to store each character's most recent index.
last_seen = {}

# Visit every character in the string using its index.
for i in range(len(text)):

    # Store the current character.
    ch = text[i]

    # Check whether the character appeared inside the current substring.
    if ch in last_seen and last_seen[ch] >= start:

        # Move the start past the previous occurrence of this character.
        start = last_seen[ch] + 1

    # Update the most recent index of the current character.
    last_seen[ch] = i

    # Calculate the length of the current substring.
    current_length = i - start + 1

    # Check whether the current substring is the longest so far.
    if current_length > max_length:

        # Update the maximum substring length.
        max_length = current_length

# Display the maximum length.
print("Longest substring length:", max_length)


# Program to search for a number using binary search.

# Take the number of elements from the user.
n = int(input("Enter the number of elements: "))

# Create an empty list to store the sorted numbers.
numbers = []

# Repeat the loop n times.
for i in range(n):

    # Take one integer from the user.
    num = int(input("Enter a number in sorted order: "))

    # Add the number to the list.
    numbers.append(num)

# Take the number to search for.
target = int(input("Enter the number to search: "))

# Set the left boundary to the first index.
left = 0

# Set the right boundary to the last index.
right = len(numbers) - 1

# Continue searching while the search area is not empty.
while left <= right:

    # Calculate the middle index.
    mid = (left + right) // 2

    # Check whether the middle number is the target.
    if numbers[mid] == target:

        # Display the index where the target was found.
        print("Number found at index:", mid)

        # Stop searching after finding the target.
        break

    # Check whether the target is greater than the middle number.
    elif target > numbers[mid]:

        # Ignore the left half and search the right half.
        left = mid + 1

    # Run this block when the target is smaller than the middle number.
    else:

        # Ignore the right half and search the left half.
        right = mid - 1

# Run this block if the loop ended without finding the target.
else:

    # Display a message if the target is not present.
    print("Number not found.")

# Program to remove duplicates while preserving order.

# Take the number of elements from the user.
n = int(input("Enter the number of elements: "))

# Create an empty list to store the numbers.
numbers = []

# Repeat the loop n times.
for i in range(n):

    # Take one integer from the user.
    num = int(input("Enter a number: "))

    # Add the number to the original list.
    numbers.append(num)

# Create an empty list to store unique numbers.
result = []

# Visit every number in the original list.
for num in numbers:

    # Check whether the number is not already in the result.
    if num not in result:

        # Add the number to the result list.
        result.append(num)

# Display the list without duplicates.
print("List after removing duplicates:", result)


# Program to find the next greater element to the right.

# Take the number of elements from the user.
n = int(input("Enter the number of elements: "))

# Create an empty list to store the numbers.
numbers = []

# Repeat the loop n times.
for i in range(n):

    # Take one integer from the user.
    num = int(input("Enter a number: "))

    # Add the number to the list.
    numbers.append(num)

# Create a result list filled with -1.
result = [-1] * n

# Create an empty stack to store indices.
stack = []

# Visit each number from left to right.
for i in range(n):

    # Check whether the stack has indices to process.
    while stack and numbers[i] > numbers[stack[-1]]:

        # Remove the index whose next greater element has been found.
        index = stack.pop()

        # Store the current number as that index's answer.
        result[index] = numbers[i]

    # Push the current index onto the stack.
    stack.append(i)

# Display the next greater elements.
print("Next greater elements:", result)



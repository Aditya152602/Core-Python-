import random

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
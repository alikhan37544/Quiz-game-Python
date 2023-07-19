import requests
import random
import html

# Getting data from the API
response = requests.get("https://opentdb.com/api.php?amount=1")
data = response.json()

## Feature 

# print(data)

## Beta feature : Ask the user to choose the category ,difficulty and type of question
# code here vvvvvvvvvvvv

# code here ^^^^^^^^^^^^^

# Categorising the data
question_data = data['results'][0]
category = question_data['category']
difficulty = question_data['difficulty']
question = question_data['question']
correct_answer = question_data['correct_answer']
incorrect_answers = question_data['incorrect_answers']

# "Unescaping" the characters for proper display
question_data, category, difficulty, question, correct_answer, incorrect_answers = html.unescape(question_data), html.unescape(category), html.unescape(difficulty), html.unescape(question), html.unescape(correct_answer), html.unescape(incorrect_answers)

# Shuffling the options
options = [correct_answer]
for char in incorrect_answers:
    options.append(char)
random.shuffle(options)

print(f"The question is from {category}")

print(f"The question is classified as {difficulty}")

print("")
print(question)
print("")

print("Your options are as follows: ")

# Logic for checking correction
i = 1
for char in options:
    print(f"{i} : {char}")
    i += 1

user_input = int(input("Your answer: ")) - 1

print(f"Your selected options is: {options[user_input]}")

if options[user_input] == correct_answer:
    print("Congratulations, you've guessed correctly")

else: 
    print("Sorry, wrong option.")
    print(f"The correct option was {correct_answer}")
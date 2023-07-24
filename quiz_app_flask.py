from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Global variables to store quiz data
category = ""
difficulty = ""
question = ""
correct_answer = ""
incorrect_answers = []

# Function to fetch a new quiz question from the API
def fetch_question():
    global category, difficulty, question, correct_answer, incorrect_answers

    # Fetch data from the API
    response = requests.get('https://opentdb.com/api.php?amount=1')
    data = response.json()

    # Extract question data from the response
    question_data = data['results'][0]
    category = question_data['category']
    difficulty = question_data['difficulty']
    question = question_data['question']
    correct_answer = question_data['correct_answer']
    incorrect_answers = question_data['incorrect_answers']

# Route for the home page
@app.route('/')
def home():
    fetch_question()  # Fetch the initial question
    return render_template('index.html', category=category, difficulty=difficulty, question=question, options=incorrect_answers + [correct_answer])

# Route to check the user's answer
@app.route('/check_answer', methods=['POST'])
def check_answer():
    user_answer = request.form['answer']
    if user_answer == correct_answer:
        result = "Congratulations, you've guessed correctly"
    else:
        result = f"Sorry, wrong option. The correct option was {correct_answer}"
    fetch_question()  # Fetch a new question for the next round
    return render_template('index.html', category=category, difficulty=difficulty, question=question, options=incorrect_answers + [correct_answer], result=result)

if __name__ == '__main__':
    app.run(debug=True)

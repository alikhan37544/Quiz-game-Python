from flask import Flask, render_template
import requests

app = Flask(__name__)

# Global variables to store quiz data
category = ""
difficulty = ""
question = ""
correct_answer = ""
incorrect_answers = []

# Route for the home page
@app.route('/')
def home():
    return render_template('index.html')

# Route to fetch a new quiz question from the API
@app.route('/get_question')
def get_question():
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

    return ''

if __name__ == '__main__':
    app.run(debug=True)

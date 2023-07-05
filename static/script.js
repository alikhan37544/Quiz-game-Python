function fetchQuestion() {
    const questionContainer = document.getElementById('question-container');
    const resultContainer = document.getElementById('result-container');

    questionContainer.style.display = 'block';
    resultContainer.style.display = 'none';

    // Fetch question from the server
    fetch('/get_question')
        .then(response => response.text())
        .then(() => displayQuestion());
}

function displayQuestion() {
    const categoryElement = document.getElementById('category');
    const difficultyElement = document.getElementById('difficulty');
    const questionElement = document.getElementById('question');
    const answersElement = document.getElementById('answers');

    categoryElement.textContent = category;
    difficultyElement.textContent = 'Difficulty: ' + difficulty;
    questionElement.textContent = question;

    // Shuffle answers
    const answers = [correct_answer, ...incorrect_answers];
    answers.sort(() => Math.random() - 0.5);

    // Display answers
    answersElement.innerHTML = '';
    answers.forEach(answer => {
        const li = document.createElement('li');
        li.textContent = answer;
        li.addEventListener('click', checkAnswer);
        answersElement.appendChild(li);
    });
}

function checkAnswer(event) {
    const selectedAnswer = event.target.textContent;
    const resultContainer = document.getElementById('result-container');
    const resultElement = document.getElementById('result');

    // Display result
    if (selectedAnswer === correct_answer) {
        resultElement.textContent = 'Correct!';
        resultElement.style.color = 'green';
    } else {
        resultElement.textContent = 'Incorrect!';
        resultElement.style.color = 'red';
    }

    resultContainer.style.display = 'block';
    event.target.removeEventListener('click', checkAnswer);
}

const questions = [
    {
        imageSource: "images/image1.jpg",
        text: "What is shown in the image?",
        options: [
            { text: "A. Daiyan", isCorrect: true },
            { text: "B. Dihan", isCorrect: false},
            { text: "C. Miraz", isCorrect: false },
            { text: "D. Messi", isCorrect: false },
            { text: "E. Ronaldo", isCorrect: false }
        ]
    },
    // Define questions, options, and correct answers for other images...
];

const imageContainer = document.getElementById('image-container');
const quizImage = document.getElementById('quiz-image');
const questionContainer = document.getElementById('question-container');
const questionElement = document.getElementById('question');
const optionsContainer = document.getElementById('options-container');
const resultContainer = document.getElementById('result-container');
const resultMessage = document.getElementById('result-message');
const scoreDisplay = document.getElementById('score-value');

let currentQuestions = [];
let currentQuestionIndex = 0;
let score = 0;
let timer;

function getRandomQuestions() {
    const randomQuestions = [];
    const shuffledQuestions = questions.sort(() => Math.random() - 0.5);
    for (let i = 0; i < 5; i++) {
        randomQuestions.push(shuffledQuestions[i]);
    }
    return randomQuestions;
}

function displayNextQuestion() {
    if (currentQuestionIndex < currentQuestions.length) {
        const currentQuestion = currentQuestions[currentQuestionIndex];
        questionElement.textContent = currentQuestion.text;
        displayOptions(currentQuestion.options);
        startTimer(7);
        currentQuestionIndex++;
    } else {
        displayResult('Quiz complete! Your final score is: ' + score);
    }
}

function displayOptions(options) {
    optionsContainer.innerHTML = '';
    options.forEach((option, index) => {
        const optionElement = document.createElement('button');
        optionElement.textContent = option.text;
        optionElement.addEventListener('click', () => checkAnswer(option.isCorrect));
        optionsContainer.appendChild(optionElement);
    });
}

function checkAnswer(isCorrect) {
    clearInterval(timer);
    if (isCorrect) {
        score += 5;
        displayResult('Correct! You earned 5 points.');
    } else {
        displayResult('Incorrect! Moving to the next question.');
    }
    setTimeout(() => {
        resultContainer.style.display = 'none';
        scoreDisplay.textContent = score;
        displayNextQuestion();
    }, 2000);
}

function startTimer(seconds) {
    let timeLeft = seconds;
    timer = setInterval(() => {
        timeLeft--;
        if (timeLeft <= 0) {
            clearInterval(timer);
            displayResult('Time\'s up! Moving to the next question.');
            setTimeout(() => {
                resultContainer.style.display = 'none';
                displayNextQuestion();
            }, 2000);
        }
    }, 1000);
}

function displayResult(message) {
    resultMessage.textContent = message;
    resultContainer.style.display = 'block';
}

currentQuestions = getRandomQuestions();
displayNextQuestion();

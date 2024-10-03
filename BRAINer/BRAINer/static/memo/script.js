const emojis = [
    { emoji: "🍎", name: "Apple" }, { emoji: "🍌", name: "Banana" }, { emoji: "🍒", name: "Cherry" },
    { emoji: "🍇", name: "Grapes" }, { emoji: "🍉", name: "Watermelon" }, { emoji: "🍓", name: "Strawberry" },
    { emoji: "🥑", name: "Avocado" }, { emoji: "🥕", name: "Carrot" }, { emoji: "🌽", name: "Corn" },
    { emoji: "🍆", name: "Eggplant" }, { emoji: "🍔", name: "Burger" }, { emoji: "🍕", name: "Pizza" },
    { emoji: "🍟", name: "Fries" }, { emoji: "🌭", name: "Hot Dog" }, { emoji: "🍿", name: "Popcorn" },
    { emoji: "🍩", name: "Donut" }, { emoji: "🍪", name: "Cookie" }, { emoji: "🎂", name: "Cake" },
    { emoji: "🍰", name: "Pie" }, { emoji: "🍫", name: "Chocolate" }, { emoji: "🍬", name: "Candy" },
    { emoji: "🍭", name: "Lollipop" }, { emoji: "🍮", name: "Custard" }, { emoji: "🍯", name: "Honey" },
    { emoji: "🍵", name: "Tea" }, { emoji: "☕", name: "Coffee" }, { emoji: "🍼", name: "Milk" },
    { emoji: "🍹", name: "Juice" }, { emoji: "🍸", name: "Cocktail" }, { emoji: "🍺", name: "Beer" },
    { emoji: "🍾", name: "Champagne" }, { emoji: "🥂", name: "Wine" }, { emoji: "🍶", name: "Sake" },
    { emoji: "🥛", name: "Glass of Milk" }, { emoji: "🍴", name: "Fork and Knife" }, { emoji: "🥄", name: "Spoon" },
    { emoji: "🍳", name: "Frying Pan" }, { emoji: "🍲", name: "Pot of Food" }, { emoji: "🥣", name: "Bowl" },
    { emoji: "🥤", name: "Soda" }, { emoji: "🥢", name: "Chopsticks" }, { emoji: "🧂", name: "Salt" },
    { emoji: "🥫", name: "Canned Food" }, { emoji: "🍿", name: "Popcorn" }, { emoji: "🍱", name: "Bento Box" },
    { emoji: "🍚", name: "Rice" }, { emoji: "🍛", name: "Curry" }, { emoji: "🍣", name: "Sushi" }
];

const displaySection = document.getElementById('display-section');
const emojisContainer = document.getElementById('emojis');
const startButton = document.getElementById('start-button');
const displayTimer = displaySection.querySelector('#timer');

const selectionSection = document.getElementById('selection-section');
const optionsContainer = document.getElementById('options');
const submitButton = document.getElementById('submit-button');
const selectionTimer = selectionSection.querySelector('#timer');

const resultSection = document.getElementById('result-section');
const scoreDisplay = document.getElementById('score');
const restartButton = document.getElementById('restart-button');

let displayedEmojis = [];
let selectedOptions = [];
let memorizationInterval;
let selectionInterval;

function getRandomEmojis(count) {
    const shuffled = emojis.sort(() => 0.5 - Math.random());
    return shuffled.slice(0, count);
}

function showEmojis() {
    displayedEmojis = getRandomEmojis(15);
    displayedEmojis.forEach(item => {
        const div = document.createElement('div');
        div.classList.add('emoji-card');
        div.innerHTML = `<span>${item.emoji}</span><span>${item.name}</span>`;
        emojisContainer.appendChild(div);
    });
}

function startGame() {
    displaySection.classList.remove('hidden');
    selectionSection.classList.add('hidden');
    resultSection.classList.add('hidden');
    emojisContainer.innerHTML = '';
    optionsContainer.innerHTML = '';
    selectedOptions = [];
    showEmojis();
    startTimer(displayTimer, 30, () => {
        displaySection.classList.add('hidden');
        selectionSection.classList.remove('hidden');
        showOptions();
        startTimer(selectionTimer, 30, () => {
            submitAnswers();
        });
    });
}

function showOptions() {
    const options = getRandomEmojis(30);
    options.forEach(item => {
        const div = document.createElement('div');
        div.classList.add('option-card');
        div.textContent = item.name;
        div.addEventListener('click', () => selectOption(div, item.name));
        optionsContainer.appendChild(div);
    });
}

function selectOption(div, name) {
    if (div.classList.contains('selected')) {
        div.classList.remove('selected');
        selectedOptions = selectedOptions.filter(option => option !== name);
    } else if (selectedOptions.length < 15) {
        div.classList.add('selected');
        selectedOptions.push(name);
    }
}

function submitAnswers() {
    let score = 0;
    displayedEmojis.forEach(item => {
        if (selectedOptions.includes(item.name)) {
            score++;
        }
    });
    scoreDisplay.textContent = score;
    selectionSection.classList.add('hidden');
    resultSection.classList.remove('hidden');
}

function startTimer(element, duration, callback) {
    let timeLeft = duration;
    element.textContent = `Time: ${timeLeft}s`;
    const interval = setInterval(() => {
        timeLeft--;
        element.textContent = `Time: ${timeLeft}s`;
        if (timeLeft <= 0) {
            clearInterval(interval);
            callback();
        }
    }, 1000);
}

startButton.addEventListener('click', startGame);
submitButton.addEventListener('click', submitAnswers);
restartButton.addEventListener('click', startGame);

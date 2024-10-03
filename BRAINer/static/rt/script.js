    let startTime;
    let endTime;
    let timeout;
    let trials = [];
    const maxTrials = 5;
    let isPaused = false;

    function startTest() {
        if (trials.length === 0) {
            document.getElementById('result').innerHTML = '';
        }
        document.getElementById('screen').style.backgroundColor = 'red';
        document.getElementById('instructions').innerText = 'Wait for green...';
        document.getElementById('startButton').style.display = 'none';
        document.getElementById('retryButton').style.display = 'none';
        document.getElementById('saveButton').style.display = 'none';
        document.getElementById('popup').style.display = 'none';

        timeout = setTimeout(() => {
            document.getElementById('screen').style.backgroundColor = 'green';
            document.getElementById('instructions').innerText = 'Click!';
            startTime = new Date().getTime();
        }, Math.floor(Math.random() * 3000) + 2000); // Random delay between 2-7 seconds
    }

    function handleClick() {
        if (isPaused) {
            isPaused = false;
            document.getElementById('popup').style.display = 'none';
            startTest();
            return;
        }

        if (document.getElementById('screen').style.backgroundColor === 'green') {
            endTime = new Date().getTime();
            let reactionTime = endTime - startTime;
            trials.push(reactionTime);
            updateResultDisplay();

            if (trials.length >= maxTrials) {
                let averageTime = trials.reduce((a, b) => a + b) / trials.length;
                document.getElementById('result').innerHTML += `<br>Average time after ${maxTrials} trials: ${averageTime.toFixed(2)} ms`;
                document.getElementById('retryButton').style.display = 'block';
                document.getElementById('saveButton').style.display = 'block';
                trials = []; // Reset trials after showing the average score
            } else {
                isPaused = true;
                document.getElementById('popup').style.display = 'block';
                document.getElementById('instructions').innerText = 'Click to resume the next trial.';
            }
        } else if (document.getElementById('screen').style.backgroundColor === 'red') {
            clearTimeout(timeout);
            document.getElementById('instructions').innerText = 'Too soon! Wait for green.';
            setTimeout(() => {
                isPaused = true;
                document.getElementById('popup').style.display = 'block';
                document.getElementById('instructions').innerText = 'Click to resume the next trial.';
            }, 1000); // Start next trial after 1 second delay
        }
    }

    function updateResultDisplay() {
        let resultText = trials.map((time, index) => `Trial ${index + 1}: ${time} ms`).join('<br>');
        document.getElementById('result').innerHTML = resultText;
    }

    function retryTest() {
        trials = [];
        document.getElementById('result').innerText = '';
        document.getElementById('retryButton').style.display = 'none';
        document.getElementById('saveButton').style.display = 'none';
        isPaused = false;
        startTest();
    }

    function saveScore() {
        let averageTime = trials.reduce((a, b) => a + b) / trials.length;
        alert(`Your average reaction time of ${averageTime.toFixed(2)} ms has been saved.`);
    }

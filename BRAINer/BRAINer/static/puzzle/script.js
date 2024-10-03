const imageSource = "images/daiyan.jpg"; // Set your image source here
const gridSize = 4; // Size of the grid (4x4)
const tileSize = 100; // Size of each tile in pixels

let puzzle = [];
let emptyIndex;

const puzzleContainer = document.getElementById("puzzle-container");
const actualImageContainer = document.getElementById("actual-image-container");

// Function to create puzzle pieces
function createPuzzle() {
    for (let i = 0; i < gridSize * gridSize; i++) {
        const tile = document.createElement("div");
        tile.classList.add("tile");
        const row = Math.floor(i / gridSize);
        const col = i % gridSize;
        if (i === gridSize * gridSize - 1) {
            tile.classList.add("empty");
            emptyIndex = i;
        } else {
            tile.style.backgroundImage = `url(${imageSource})`;
            tile.style.backgroundPosition = `-${col * tileSize}px -${row * tileSize}px`;
        }
        tile.setAttribute("data-index", i);
        puzzleContainer.appendChild(tile);
        puzzle.push(tile);
    }
}

// Function to shuffle the puzzle pieces
function shufflePuzzle() {
    for (let i = puzzle.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        const temp = puzzle[i];
        puzzle[i] = puzzle[j];
        puzzle[j] = temp;
    }
    emptyIndex = puzzle.findIndex(tile => tile.classList.contains("empty"));
    updatePuzzle();
}

// Function to move the puzzle piece
function moveTile(index) {
    const row = Math.floor(index / gridSize);
    const col = index % gridSize;
    const emptyRow = Math.floor(emptyIndex / gridSize);
    const emptyCol = emptyIndex % gridSize;

    if ((row === emptyRow && Math.abs(col - emptyCol) === 1) || (col === emptyCol && Math.abs(row - emptyRow) === 1)) {
        const temp = puzzle[index];
        puzzle[index] = puzzle[emptyIndex];
        puzzle[emptyIndex] = temp;
        emptyIndex = index;
        updatePuzzle();
    }

    if (isSolved()) {
        alert("Congratulations! You solved the puzzle!");
    }
}

// Function to update the puzzle grid
function updatePuzzle() {
    puzzleContainer.innerHTML = "";
    for (const tile of puzzle) {
        puzzleContainer.appendChild(tile);
    }
}

// Function to check if puzzle is solved
function isSolved() {
    for (let i = 0; i < puzzle.length; i++) {
        if (parseInt(puzzle[i].dataset.index) !== i) {
            return false;
        }
    }
    return true;
}

// Event listeners for arrow key presses
document.addEventListener("keydown", (event) => {
    if (event.key === "ArrowLeft" && emptyIndex % gridSize !== gridSize - 1) {
        moveTile(emptyIndex + 1);
    } else if (event.key === "ArrowRight" && emptyIndex % gridSize !== 0) {
        moveTile(emptyIndex - 1);
    } else if (event.key === "ArrowUp" && emptyIndex < gridSize * (gridSize - 1)) {
        moveTile(emptyIndex + gridSize);
    } else if (event.key === "ArrowDown" && emptyIndex >= gridSize) {
        moveTile(emptyIndex - gridSize);
    }
});

// Event listener for start button
document.getElementById("start-btn").addEventListener("click", () => {
    createPuzzle();
    shufflePuzzle(); // Shuffle the puzzle pieces when starting the game
});

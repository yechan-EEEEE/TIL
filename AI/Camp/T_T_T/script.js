
const game = document.getElementById('game');
const resetBtn = document.getElementById('reset');
const modeToggle = document.getElementById('mode-toggle');
const playerForm = document.getElementById('player-form');
const playerXInput = document.getElementById('playerX');
const playerOInput = document.getElementById('playerO');
const controls = document.getElementById('controls');
const scoreboard = document.getElementById('scoreboard');
let board = Array(9).fill('');
let currentPlayer = 'X';
let gameActive = true;
let playerNames = { X: 'X', O: 'O' };

function render() {
    game.innerHTML = '';
    // Update scoreboard
    if (gameActive) {
        scoreboard.textContent = `${playerNames[currentPlayer]} (${currentPlayer}) 차례`;
    } else {
        if (checkWin()) {
            scoreboard.textContent = `${playerNames[currentPlayer]} (${currentPlayer}) 승리!`;
        } else {
            scoreboard.textContent = '무승부!';
        }
    }
    // Draw cells
    const boardDiv = document.createElement('div');
    boardDiv.style.display = 'grid';
    boardDiv.style.gridTemplateColumns = 'repeat(3, 160px)';
    boardDiv.style.gridTemplateRows = 'repeat(3, 160px)';
    boardDiv.style.gap = '20px';
    board.forEach((cell, i) => {
        const div = document.createElement('div');
        div.className = 'cell';
        div.textContent = cell;
        div.onclick = () => handleClick(i);
        boardDiv.appendChild(div);
    });
    game.appendChild(boardDiv);
}

function handleClick(i) {
    if (!gameActive || board[i]) return;
    board[i] = currentPlayer;
    if (checkWin()) {
        gameActive = false;
    } else if (board.every(cell => cell)) {
        gameActive = false;
    } else {
        currentPlayer = currentPlayer === 'X' ? 'O' : 'X';
    }
    render();
}

function checkWin() {
    const wins = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ];
    return wins.some(line => {
        const [a,b,c] = line;
        return board[a] && board[a] === board[b] && board[a] === board[c];
    });
}

resetBtn.onclick = () => {
    board = Array(9).fill('');
    currentPlayer = 'X';
    gameActive = true;
    render();
};

// Player name form
playerForm.onsubmit = function(e) {
    e.preventDefault();
    playerNames.X = playerXInput.value || 'X';
    playerNames.O = playerOInput.value || 'O';
    playerForm.style.display = 'none';
    game.style.display = '';
    controls.style.display = 'flex';
    board = Array(9).fill('');
    currentPlayer = 'X';
    gameActive = true;
    render();
};

// Dark/Light Mode Toggle
function setMode(isDark) {
    document.body.classList.toggle('dark', isDark);
    modeToggle.checked = isDark;
    localStorage.setItem('ttt-mode', isDark ? 'dark' : 'light');
}

modeToggle.addEventListener('change', () => {
    setMode(modeToggle.checked);
});

// On load, set mode from localStorage
const savedMode = localStorage.getItem('ttt-mode');
if (savedMode === 'dark') {
    setMode(true);
} else {
    setMode(false);
}

// Hide game and controls at first
game.style.display = 'none';
controls.style.display = 'none';

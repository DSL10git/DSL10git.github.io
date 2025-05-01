const canvas = document.getElementById("chessboard");
const ctx = canvas.getContext("2d");
const tileSize = 80;
const boardSize = 8;
let selectedPiece = null;
let turn = "white";

const board = [
    ["r", "n", "b", "q", "k", "b", "n", "r"],
    ["p", "p", "p", "p", "p", "p", "p", "p"],
    ["", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", ""],
    ["P", "P", "P", "P", "P", "P", "P", "P"],
    ["R", "N", "B", "Q", "K", "B", "N", "R"]
];

const pieceImages = {};
const pieceMap = {
    "p": "black_pawn", "r": "black_rook", "n": "black_knight", "b": "black_bishop", "q": "black_queen", "k": "black_king",
    "P": "white_pawn", "R": "white_rook", "N": "white_knight", "B": "white_bishop", "Q": "white_queen", "K": "white_king"
};

function loadImages() {
    for (const key in pieceMap) {
        const img = new Image();
        img.src = `images/${pieceMap[key]}.png`;
        pieceImages[key] = img;
    }
}

function drawBoard() {
    for (let row = 0; row < boardSize; row++) {
        for (let col = 0; col < boardSize; col++) {
            ctx.fillStyle = (row + col) % 2 === 0 ? "#f0d9b5" : "#b58863";
            ctx.fillRect(col * tileSize, row * tileSize, tileSize, tileSize);
            const piece = board[row][col];
            if (piece) {
                ctx.drawImage(pieceImages[piece], col * tileSize, row * tileSize, tileSize, tileSize);
            }
        }
    }
}

canvas.addEventListener("click", (event) => {
    const col = Math.floor(event.offsetX / tileSize);
    const row = Math.floor(event.offsetY / tileSize);
    handleMove(row, col);
});

function handleMove(row, col) {
    if (!selectedPiece) {
        if (board[row][col] && isCorrectTurn(board[row][col])) {
            selectedPiece = { row, col, piece: board[row][col] };
        }
    } else {
        if (isValidMove(selectedPiece, row, col)) {
            board[row][col] = selectedPiece.piece;
            board[selectedPiece.row][selectedPiece.col] = "";
            turn = turn === "white" ? "black" : "white";
        }
        selectedPiece = null;
    }
    drawBoard();
}

function isCorrectTurn(piece) {
    return (turn === "white" && piece === piece.toUpperCase()) || (turn === "black" && piece === piece.toLowerCase());
}

function isValidMove(piece, newRow, newCol) {
    // Basic move validation (pawn movement, check, etc. to be added later)
    return true;
}

loadImages();
drawBoard();
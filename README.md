# FEN Validator - Chess Notation Validator

The **FEN Validator** is a Python application built with PyQt5 that validates and visualizes FEN (Forsyth-Edwards Notation) strings for chessboard configurations. In addition to validating FEN syntax, the application graphically displays the arrangement of pieces on the board.

---

## 📋 Features

- **FEN Validation**: Checks if a FEN string is valid according to chess rules.
- **Board Visualization**: Displays the chessboard with pieces based on the FEN string.
- **Predefined Examples**: Includes examples of valid and invalid FEN strings for testing.
- **Graphical Interface**: Built with PyQt5, offering an intuitive user experience.

---

## 🛠️ Requirements

To run this project, you need:

- **Python 3.8 or higher**.
- **PyQt5**: For the graphical interface.
- **Additional Libraries**: `re` (regular expressions) and `random`.

### Installing Dependencies

```bash
pip install PyQt5
```

## 🚀 How to Use

### Clone the repository:
```bash
git clone https://github.com/santig005/FEN-Validator.git
cd FEN-Validator
```
### Run the application:

```bash
python app.py
```
## User Interface:

Enter a FEN string in the input field.

The application will automatically validate the FEN string and display the corresponding board.

If the notation is invalid, a detailed error message will be shown.

## FEN Examples
The application includes buttons to load predefined examples:

### Starting Position:

```bash
rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1
```
### Scholar's Mate:

```bash
r1bqk1nr/pppp1Qpp/2n5/2b1p3/2B1P3/8/PPPP1PPP/RNB1K1NR b KQkq - 0 4
```
### Alternating Queens:

```bash
QqQqQqQq/qQqQqQqQ/QqQqQqQq/qQqQqQqQ/QqQqQqQq/qQqQqQqQ/QqQqQqQq/qQqQqQqQ b - - 0 4
```
### Invalid FEN:

```bash
8/6.app/p1n2k2/1fp6/3N#P/1q6/5K2/8 s qk e6 51 1
```

## 🧠 How It Works
### FEN Validation
The application uses regular expressions to validate FEN syntax. It checks:

FEN Structure: 8 rows separated by /.

Pieces and Numbers: Each row must sum to 8 squares (pieces or numbers indicating empty squares).

Additional Details: Turn, castling rights, en passant, etc

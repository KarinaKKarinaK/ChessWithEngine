# ChessWithEngine

A Python chess game with a GUI (using Pygame) and Stockfish engine integration for computer play.

## Features

- Play chess against the Stockfish engine
- Pygame-based graphical interface
- Human vs. Computer or Human vs. Human
- Move validation and FEN export
- Adjustable engine skill level

## Requirements

- Python 3.9+
- [Stockfish](https://stockfishchess.org/download/)
- [pygame](https://www.pygame.org/)
- [python-stockfish](https://pypi.org/project/stockfish/)

Install dependencies:
```sh
pip install -r requirements.txt
```

## Setup

1. **Download Stockfish**  
   Download the Stockfish binary for your OS and architecture from [stockfishchess.org](https://stockfishchess.org/download/).

2. **Place Stockfish Binary**  
   Place the Stockfish binary in the `stockfish/` directory of this project.  
   Example:  
   ```
   ChessWithEngine/
     stockfish/
       stockfish-macos-m1-apple-silicon
   ```

3. **Make Stockfish Executable (macOS/Linux only):**
   ```sh
   chmod +x stockfish/stockfish-macos-m1-apple-silicon
   ```

4. **Check the Stockfish Path**  
   Ensure the path in `src/engine.py` matches the location and name of your Stockfish binary.

## Running the Game

From the project root, run:
```sh
python src/main.py
```

## How to Play

- Drag and drop pieces to make your move.
- The engine will respond automatically on its turn.
- Moves are validated and illegal moves are not allowed.

## File Structure

```
ChessWithEngine/
├── src/
│   ├── main.py
│   ├── game.py
│   ├── engine.py
│   ├── board.py
│   ├── ...
├── stockfish/
│   └── stockfish-macos-m1-apple-silicon
├── requirements.txt
└── README.md
```

## Customization

- **Skill Level:**  
  Change the engine skill level in `src/engine.py`:
  ```python
  stockfish.set_skill_level(15)  # 0 (weakest) to 20 (strongest)
  ```

- **ELO Rating:**  
  Alternatively, set an ELO rating:
  ```python
  stockfish.set_elo_rating(1350)
  ```

## Troubleshooting

- **FileNotFoundError:**  
  Make sure the Stockfish binary path is correct and the file is executable.

- **Pygame Issues:**  
  Ensure you have the correct version of Pygame installed for your Python version.

## License

This project is for educational purposes.

---
```# ChessWithEngine

A Python chess game with a GUI (using Pygame) and Stockfish engine integration for computer play.

## Features

- Play chess against the Stockfish engine
- Pygame-based graphical interface
- Human vs. Computer or Human vs. Human
- Move validation and FEN export
- Adjustable engine skill level

## Requirements

- Python 3.9+
- [Stockfish](https://stockfishchess.org/download/)
- [pygame](https://www.pygame.org/)
- [python-stockfish](https://pypi.org/project/stockfish/)

Install dependencies:
```sh
pip install -r requirements.txt
```

## Setup

1. **Download Stockfish**  
   Download the Stockfish binary for your OS and architecture from [stockfishchess.org](https://stockfishchess.org/download/).

2. **Place Stockfish Binary**  
   Place the Stockfish binary in the `stockfish/` directory of this project.  
   Example:  
   ```
   ChessWithEngine/
     stockfish/
       stockfish-macos-m1-apple-silicon
   ```

3. **Make Stockfish Executable (macOS/Linux only):**
   ```sh
   chmod +x stockfish/stockfish-macos-m1-apple-silicon
   ```

4. **Check the Stockfish Path**  
   Ensure the path in `src/engine.py` matches the location and name of your Stockfish binary.

## Running the Game

From the project root, run:
```sh
python src/main.py
```

## How to Play

- Drag and drop pieces to make your move.
- The engine will respond automatically on its turn.
- Moves are validated and illegal moves are not allowed.

## File Structure

```
ChessWithEngine/
├── src/
│   ├── main.py
│   ├── game.py
│   ├── engine.py
│   ├── board.py
│   ├── ...
├── stockfish/
│   └── stockfish-macos-m1-apple-silicon
├── requirements.txt
└── README.md
```

## Customization

- **Skill Level:**  
  Change the engine skill level in `src/engine.py`:
  ```python
  stockfish.set_skill_level(15)  # 0 (weakest) to 20 (strongest)
  ```

- **ELO Rating:**  
  Alternatively, set an ELO rating:
  ```python
  stockfish.set_elo_rating(1350)
  ```

## Troubleshooting

- **FileNotFoundError:**  
  Make sure the Stockfish binary path is correct and the file is executable.

- **Pygame Issues:**  
  Ensure you have the correct version of Pygame installed for your Python version.

## License

This project is for educational purposes.

---
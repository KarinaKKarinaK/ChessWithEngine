from stockfish import Stockfish
from board import Board

stockfish = Stockfish(path="../stockfish/stockfish-macos-m1-apple-silicon", depth=18, parameters={"Threads": 2, "Minimum Thinking Time": 30})
stockfish.set_skill_level(15)

board = Board()
fen = board.get_fen()

# or use thsi to set the ELO rating instead of skill level:
# stockfish.set_elo_rating(1350)
def sync_engine_with_board(board: Board, turn: str = 'w', castling: str = 'KQkq', en_passant: str = '-', halfmove: int = 0, fullmove: int = 1):
    fen = board.get_fen(turn, castling, en_passant, halfmove, fullmove)
    stockfish.set_fen_position(fen)

def set_position_from_fen(fen: str) -> None:
    stockfish.set_fen_position(fen)

def set_position_from_moves(moves: list[str]) -> None:
    stockfish.set_position(moves)

def get_best_move() -> str | None:
    """
    Returns the best move in UCI format (e.g., 'e2e4') for the current position.
    Returns None if no move is found.
    """
    return stockfish.get_best_move()

def play_move(move_uci: str, board: Board):
    """
    Plays a move on both the internal board and the Stockfish engine.
    Args:
        move_uci: Move in UCI format, e.g., 'e2e4'
        board: Board instance
    """
    # Parse UCI move
    from_square = move_uci[:2]
    to_square = move_uci[2:4]

    # Convert algebraic notation to indices
    col_map = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}
    from_col = col_map[from_square[0]]
    from_row = 8 - int(from_square[1])
    to_col = col_map[to_square[0]]
    to_row = 8 - int(to_square[1])

    # Get the piece and create a Move object
    piece = board.squares[from_row][from_col].piece
    if piece is None:
        raise ValueError(f"No piece at {from_square}")

    from move import Move
    from square import Square

    initial = Square(from_row, from_col, piece)
    final = Square(to_row, to_col, board.squares[to_row][to_col].piece)
    move = Move(initial, final)

    # Update your board
    board.move(piece, move)

    # Update Stockfish
    stockfish.make_moves_from_current_position([move_uci])

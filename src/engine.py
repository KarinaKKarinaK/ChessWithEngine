from stockfish import Stockfish

stockfish = Stockfish(path="../stockfish/stockfish-macos-m1-apple-silicon", depth=18, parameters={"Threads": 2, "Minimum Thinking Time": 30})
stockfish.set_skill_level(15)

# or use thsi to set the ELO rating instead of skill level:
# stockfish.set_elo_rating(1350)
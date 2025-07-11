import pygame
import sys

from const import *
from game import Game
from square import Square
from move import Move
from engine import sync_engine_with_board, get_best_move, play_move

class Main:

    def __init__(self): #Always called when we create an object
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Chess')
        self.game = Game()

    def mainloop(self):

        game = self.game
        board = self.game.board
        screen = self.screen
        dragger = self.game.dragger

        while True:
            # Show methods
            game.show_bg(screen)
            game.show_last_move(screen)
            game.show_moves(screen)
            game.show_pieces(screen)

            game.show_hover(screen)

            if dragger.dragging:
                dragger.update_blit(screen)

            for event in pygame.event.get():

                # Our click event
                if event.type == pygame.MOUSEBUTTONDOWN:
                    dragger.update_mouse(event.pos)
                    
                    clicked_row = dragger.mouseY // SQSIZE
                    clicked_col = dragger.mouseX // SQSIZE

                    # Asking if square has a piece
                    if board.squares[clicked_row][clicked_col].has_piece():
                        piece =  board.squares[clicked_row][clicked_col].piece
                        # Check if its a valid piece (color)
                        if piece.color == game.next_player:
                            board.calc_moves(piece, clicked_row, clicked_col, bool=True)
                            dragger.save_initial(event.pos)
                            dragger.drag_piece(piece)

                            # Show methods
                            game.show_bg(screen)
                            game.show_last_move(screen)
                            game.show_moves(screen)
                            game.show_pieces(screen)

                # Mouse motion
                elif event.type == pygame.MOUSEMOTION:
                    motion_row = event.pos[1] // SQSIZE
                    motion_col = event.pos[0] // SQSIZE

                    game.set_hover(motion_row, motion_col)

                    if dragger.dragging:
                        dragger.update_mouse(event.pos)
                        # Show methods
                        game.show_bg(screen)
                        game.show_last_move(screen)
                        game.show_moves(screen)
                        game.show_pieces(screen)
                        game.show_hover(screen) 
                        dragger.update_blit(screen)
                
                # Click release
                elif event.type == pygame.MOUSEBUTTONUP:
                    if dragger.dragging:
                        dragger.update_mouse(event.pos)
                        released_row = dragger.mouseY // SQSIZE
                        released_col = dragger.mouseX // SQSIZE

                        initial = Square(dragger.initial_row, dragger.initial_col)
                        final = Square(released_row, released_col)
                        move = Move(initial, final)

                        if board.valid_move(dragger.piece, move):
                            captured = board.squares[released_row][released_col].has_piece()
                            board.move(dragger.piece, move)
                            board.set_true_en_pessant(dragger.piece)
                            game.play_sound(captured)
                            game.show_bg(screen)
                            game.show_last_move(screen)
                            game.show_pieces(screen)
                            game.next_turn()

                            # --- ENGINE TURN ---
                            # Sync Stockfish with the new board state
                            sync_engine_with_board(board, turn=game.next_player[0])
                            # If it's the computer's turn, get and play the engine move
                            if game.next_player == "black":  # or "white" if you want engine as white
                                engine_move = get_best_move()
                                if engine_move:
                                    play_move(engine_move, board)
                                    game.next_turn()

                    dragger.undrag_piece()
                
                #Key press
                elif event.type == pygame.KEYDOWN:

                    # Changing theme with 't'
                    if event.key == pygame.K_t:
                        game.change_theme()

                    # Restarting with 'r'
                    if event.key == pygame.K_r:
                        game.reset()

                        game = self.game
                        board = self.game.board 
                        dragger = self.game.dragger


                # Quit game
                elif event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            pygame.display.update()

main = Main()
main.mainloop()
import board
import unittests

"Setting game variables"

BOARD_HEIGHT = 10
BOARD_WIDTH = 10

new_game_board = board.random_state(BOARD_HEIGHT, BOARD_WIDTH)

board.render(new_game_board)

next_board = board.next_board_state(new_game_board)

board.render(next_board)

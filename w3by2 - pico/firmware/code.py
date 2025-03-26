import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation

keyboard = KMKKeyboard()

keyboard.col_pins = (board.GP20, board.GP19, board.GP18) # Cols
keyboard.row_pins = (board.GP17, board.GP16)             # Rows
keyboard.diode_orientation = DiodeOrientation.COL2ROW

# Keymap
keyboard.keymap = [
    [KC.F18, KC.F19, KC.F20, KC.F15, KC.F16, KC.F17]
]

if __name__ == '__main__':
    keyboard.go()

from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard
from kmk.scanners import DiodeOrientation

from kmk.quickpin.pro_micro.sparkfun_promicro_rp2040 import pinout as pins

class KMKKeyboard(_KMKKeyboard):
    row_pins = (
        pins[6],
        pins[10],
        pins[11]
    )
    
    col_pins = (
        pins[8],
        pins[9],
        pins[7],
        pins[12],
        pins[13],
        pins[14],
        pins[15],
        pins[16],
        pins[17],
        pins[18]
    )

    diode_orientation = DiodeOrientation.COL2ROW
    rgb_pixel_pin = pins[19]
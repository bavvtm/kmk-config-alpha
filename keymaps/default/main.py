from kb import KMKKeyboard

from kmk.keys import KC
from kmk.modules.layers import Layers
from kmk.modules.modtap import ModTap
from kmk.extensions.rgb import RGB
from kmk.handlers.sequences import send_string

keyboard = KMKKeyboard()

layers_ext = Layers()
modtap = ModTap()
rgb = RGB(pixel_pin=KMKKeyboard.rgb_pixel_pin, num_pixels=20)

keyboard.modules = [layers_ext, modtap]
keyboard.extensions = [rgb]
keyboard.debug_enabled = True

# Key names
_______ = KC.TRNS
XXXXXXX = KC.NO
HOME = KC.TO(0)
MODS = KC.TO(1)
MODS2 = KC.TO(2)
OTHER = KC.TO(3)
MTSLS = KC.MT(KC.SPC, KC.LSFT)
MTELS = KC.MT(KC.ENTER, KC.LSFT)
MACRO1 = send_string("I'm so sorry... -PyrsoL")

keyboard.keymap = [
    # HOME
    # ,---------------------------------------------------------------------.
    # |   Q  |   W  |   E  |   R  |   T  |   Y  |   U  |   I  |   O  |   P  |
    # |------+------+------+------+------+-------------+------+------+------|
    # |   A  |   S  |   D  |   F  |   G  |   H  |   J  |   K  |   L  | MODS |
    # |------+------+------+------+------+------+------+------+------+------|
    # |   Z  |   X  |   C  |   V  |XXXXXX| MTSLS|XXXXXX|   B  |   N  |   M  |
    # |------+------+------+------+------+------+------+------+------+------|
  [
    KC.Q, KC.W, KC.E, KC.R, KC.T, KC.Y, KC.U, KC.I, KC.O, KC.P, \
    KC.A, KC.S, KC.D, KC.F, KC.G, KC.H, KC.J, KC.K, KC.L, MODS, \
    KC.Z, KC.X, KC.C, KC.V, XXXXXXX, MTSLS, XXXXXXX, KC.B, KC.N, KC.M,
  ],
    # MODS
    # ,---------------------------------------------------------------------.
    # |   1  |   2  |   3  |   4  |   5  |   6  |   7  |   8  |   9  |   0  |
    # |------+------+------+------+------+-------------+------+------+------|
    # | BSPC |  ESC |  TAB |   ;  |   '  | LEFT | DOWN |  UP  | RIGHT| MODS2|
    # |------+------+------+------+------+------+------+------+------+------|
    # | LCTRL|  LGUI|  LALT|QWERTY|XXXXXX| MTELS|XXXXXX|   ,  |   .  |   /  |
    # |------+------+------+------+------+------+------+------+------+------|
  [
    KC.N1, KC.N2, KC.N3, KC.N4, KC.N5, KC.N6, KC.N7, KC.N8, KC.N9, KC.N0, \
    KC.BSPC, KC.GESC, KC.TAB, KC.SCLN, KC.QUOT, KC.LEFT, KC.DOWN, KC.UP, KC.RIGHT, MODS2, \
    KC.LCTRL, KC.LGUI, KC.LALT, HOME, XXXXXXX, MTELS, XXXXXXX, KC.COMM, KC.DOT, KC.SLSH,
  ],
    # MODS2
    # ,---------------------------------------------------------------------.
    # |  F1  |  F2  |  F3  |  F4  |  F5  |  F6  |  F7  |  F8  |  F9  |  F10 |
    # |------+------+------+------+------+-------------+------+------+------|
    # | LSFT |  F11 |  F12 |   -  |   =  |   [  |   ]  |   \  |   `  | OTHER|
    # |------+------+------+------+------+------+------+------+------+------|
    # | RGB+ | RGB- |RGBHUI|QWERTY|XXXXXX|RGBMOD|XXXXXX| PLAY | VOLD | VOLU |
    # |------+------+------+------+------+------+------+------+------+------|
  [
    KC.F1, KC.F2, KC.F3, KC.F4, KC.F5, KC.F6, KC.F7, KC.F8, KC.F9, KC.F10, \
    KC.LSFT, KC.F11, KC.F12, KC.MINS, KC.EQUAL, KC.LBRC, KC.RBRC, KC.BSLASH, KC.GRV, OTHER, \
    KC.RGB_VAI, KC.RGB_VAD, KC.RGB_HUI, HOME, XXXXXXX, KC.RGB_M_P, XXXXXXX, KC.MPLY, KC.VOLD, KC.VOLU,
  ],
    # OTHER
    # ,---------------------------------------------------------------------.
    # | RESET|XXXXXX|XXXXXX|XXXXXX|XXXXXX|XXXXXX|XXXXXX|XXXXXX|XXXXXX|XXXXXX|
    # |------+------+------+------+------+-------------+------+------+------|
    # |XXXXXX|XXXXXX|XXXXXX|XXXXXX|XXXXXX|XXXXXX|XXXXXX|XXXXXX|XXXXXX|XXXXXX|
    # |------+------+------+------+------+------+------+------+------+------|
    # |XXXXXX|XXXXXX|XXXXXX|QWERTY|XXXXXX|MACRO1|XXXXXX|XXXXXX|XXXXXX|XXXXXX|
    # |------+------+------+------+------+------+------+------+------+------|
  [
    KC.RESET, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, \
    XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, \
    XXXXXXX, XXXXXXX, XXXXXXX, HOME, XXXXXXX, MACRO1, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,
  ]
]

if __name__ == '__main__':
  keyboard.go()
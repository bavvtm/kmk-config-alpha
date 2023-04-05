from kb import KMKKeyboard

from kmk.keys import KC
from kmk.modules.layers import Layers
from kmk.modules.modtap import ModTap

keyboard = KMKKeyboard()

layers_ext = Layers()
modtap = ModTap()

keyboard.modules = [layers_ext, modtap]
keyboard.debug_enabled = True

# Key names
_______ = KC.TRNS
XXXXXXX = KC.NO

MTZCTL = KC.MT(KC.Z, KC.LCTRL)
MTXALT = KC.MT(KC.X, KC.LALT)
LT2C = KC.LT(2, KC.C)
LT1V = KC.LT(1, KC.V)
MTSLS = KC.MT(KC.SPC, KC.LSFT)
MTBWIN = KC.MT(KC.B, KC.LWIN)
MTNALT = KC.MT(KC.N, KC.RALT)
MTMCTL = KC.MT(KC.M, KC.RCTRL)

keyboard.keymap = [
    # HOME
    # ,---------------------------------------------------------------------.
    # |   Q  |   W  |   E  |   R  |   T  |   Y  |   U  |   I  |   O  |   P  |
    # |------+------+------+------+------+-------------+------+------+------|
    # |   A  |   S  |   D  |   F  |   G  |   H  |   J  |   K  |   L  | ENTER|
    # |------+------+------+------+------+------+------+------+------+------|
    # |MTZCTL|MTXALT| LT2C | LT1V |XXXXXX| MTSLS|XXXXXX|MTBWIN|MTNALT|MTMCTL|
    # |------+------+------+------+------+------+------+------+------+------|
  [
    KC.Q, KC.W, KC.E, KC.R, KC.T, KC.Y, KC.U, KC.I, KC.O, KC.P, \
    KC.A, KC.S, KC.D, KC.F, KC.G, KC.H, KC.J, KC.K, KC.L, KC.ENTER, \
    MTZCTL, MTXALT, LT2C, LT1V, XXXXXXX, MTSLS, XXXXXXX, MTBWIN, MTNALT, MTMCTL,
  ],
    # FN
    # ,---------------------------------------------------------------------.
    # |  ESC | MUTE | VOLD | VOLU | PLAY | HOME | PDOWN|  PUP |  END |XXXXXX|
    # |------+------+------+------+------+-------------+------+------+------|
    # |  TAB |XXXXXX|XXXXXX|XXXXXX|XXXXXX| LEFT | DOWN |  UP  | RIGHT| BSPC |
    # |------+------+------+------+------+------+------+------+------+------|
    # | LCTRL|  LALT| TRIM | MO(3)|XXXXXX| MTSLS|XXXXXX| RGUI | RALT | RCTL |
    # |------+------+------+------+------+------+------+------+------+------|
  [
    KC.ESC, KC.MUTE, KC.VOLD, KC.VOLU, KC.MPLY, KC.HOME, KC.PGDN, KC.PGUP, KC.END, XXXXXXX, \
    KC.TAB, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, KC.LEFT, KC.DOWN, KC.UP, KC.RIGHT, KC.BSPC, \
    KC.LCTRL, KC.LALT, _______, KC.MO(3), XXXXXXX, MTSLS, XXXXXXX, KC.RGUI, KC.RALT, KC.RCTL,
  ],
    # FNCHAR
    # ,---------------------------------------------------------------------.
    # |   1  |   2  |   3  |   4  |   5  |   6  |   7  |   8  |   9  |   0  |
    # |------+------+------+------+------+-------------+------+------+------|
    # |  GRV |XXXXXX|   -  |   =  |   \  |   [  |   ]  |   ;  |   '  | BSPC |
    # |------+------+------+------+------+------+------+------+------+------|
    # | LCTRL|  LALT| MO(3)| TRIM |XXXXXX| MTSLS|XXXXXX|   ,  |   .  |   /  |
    # |------+------+------+------+------+------+------+------+------+------|
  [
    KC.N1, KC.N2, KC.N3, KC.N4, KC.N5, KC.N6, KC.N7, KC.N8, KC.N9, KC.N0, \
    KC.GRV, XXXXXXX, KC.MINS, KC.EQUAL, KC.BSLS, KC.LBRC, KC.RBRC, KC.SCLN, KC.QUOT, KC.BSPC, \
    KC.LCTRL, KC.LALT, KC.MO(3), _______, XXXXXXX, MTSLS, XXXXXXX, KC.COMM, KC.DOT, KC.SLSH,
  ],
    # FKEYS
    # ,---------------------------------------------------------------------.
    # |  F1  |  F2  |  F3  |  F4  |  F5  |  F6  |  F7  |  F8  |  F9  |  F10 |
    # |------+------+------+------+------+-------------+------+------+------|
    # |  F11 |  F12 |XXXXXX|XXXXXX|XXXXXX|XXXXXX|XXXXXX|XXXXXX|XXXXXX|  DEL |
    # |------+------+------+------+------+------+------+------+------+------|
    # | LCTRL|  LALT| TRIM | TRIM |XXXXXX| MTSLS|XXXXXX| RGUI | RALT | RCTL |
    # |------+------+------+------+------+------+------+------+------+------|
  [
    KC.F1, KC.F2, KC.F3, KC.F4, KC.F5, KC.F6, KC.F7, KC.F8, KC.F9, KC.F10, \
    KC.F11, KC.F12, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, \
    KC.LCTRL, KC.LALT, _______, _______, XXXXXXX, MTSLS, XXXXXXX, KC.RGUI, KC.RALT, KC.RCTRL,
  ]
]

if __name__ == '__main__':
  keyboard.go()
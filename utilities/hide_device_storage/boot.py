import supervisor
import digitalio
import storage
import usb_cdc
import usb_hid

from kb import KMKKeyboard

# Supervisor usb identification settings
# See vid and pid reference, https://github.com/qmk/qmk_firmware/blob/master/keyboards/alpha/info.json
supervisor.set_usb_identification(
    manufacturer = "KMK",
    product = "KMK PyroL Alpha RP2040",
    vid = 0xFEED,
    pid = 0x6060
)

# If this key is held during boot, don't run the code which hides the storage and disables serial
# This will use the first row/col pin. Feel free to change it if you want it to be another pin
col = digitalio.DigitalInOut(KMKKeyboard.col_pins[9])
row = digitalio.DigitalInOut(KMKKeyboard.row_pins[1])

# TODO: If your diode orientation is ROW2COL, then make row the output and col the input
col.switch_to_output(value=True)
row.switch_to_input(pull=digitalio.Pull.DOWN)

if not row.value:
    storage.disable_usb_drive()
    usb_cdc.disable()
    usb_hid.enable(boot_device=1)

row.deinit()
col.deinit()
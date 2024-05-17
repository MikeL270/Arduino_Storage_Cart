# Library used to control an 8x8 LED matrix
# Written by Michael Lance
# Created: 5/16/2024
# Last Modified: 5/16/2024
#---------------------------------------------------------------------#
# Modules used for interacting with arduino
import board
import digitalio

class LedMatrix:
    def __init__(self):
        # Pin Rows
        self.PIN_ROWS = {
        1: digitalio.DigitalInOut(board.MISO),
        2: digitalio.DigitalInOut(board.A0),
        3: digitalio.DigitalInOut(board.RX),
        4: digitalio.DigitalInOut(board.A1),
        5: digitalio.DigitalInOut(board.TX),
        6: digitalio.DigitalInOut(board.A2),
        7: digitalio.DigitalInOut(board.SDA),
        8: digitalio.DigitalInOut(board.A3)
        }
        # Pin COLUMNs
        self.PIN_COLUMNS = {
        1: digitalio.DigitalInOut(board.MOSI),  
        2: digitalio.DigitalInOut(board.A5),
        3: digitalio.DigitalInOut(board.SCK),
        4: digitalio.DigitalInOut(board.A4),
        5: digitalio.DigitalInOut(board.D2),
        6: digitalio.DigitalInOut(board.D0),
        7: digitalio.DigitalInOut(board.D1),
        8: digitalio.DigitalInOut(board.SCL)
        }

        # configure each pin as output
        for pin in self.PIN_ROWS.values():
            pin.direction = digitalio.Direction.OUTPUT

        for pin in self.PIN_COLUMNS.values():
            pin.direction = digitalio.Direction.OUTPUT

    def led_on(self, ROW, COLUMN):
        # Set all pins off first
        for pin in self.PIN_ROWS.values():
            pin.value = False

        for pin in self.PIN_COLUMNS.values():
            pin.value = True

        # Turn on the selected row
        self.PIN_ROWS[ROW].value = True

        # Turn off the selected column
        self.PIN_COLUMNS[COLUMN].value = False  

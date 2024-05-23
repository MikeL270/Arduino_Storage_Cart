# Library used to control an 8x8 LED matrix
# Written by Michael Lance
# Created: 5/16/2024
# Last Modified: 5/23/2024
#---------------------------------------------------------------------#
# Modules used for interacting with an arduino
import board
import digitalio

#---------------------------------------------------------------------#

class LedMatrix:
    def __init__(self):
        # Pin Rows
        self.PIN_ROWS = {}
        # Pin Columns
        self.PIN_COLUMNS = {}

    def led_on(self, ROW, COLUMN):
        # Set all pins off first
        for pin in self.PIN_ROWS.values():
            pin.value = True

        for pin in self.PIN_COLUMNS.values():
            pin.value = False

        # Turn on the selected power pin to true
        self.PIN_COLUMNS[COLUMN].value = True

        # Set the selected ground pin to false
        self.PIN_ROWS[ROW].value = False

#---------------------------------------------------------------------#

class Board1(LedMatrix):
    def __init__(self):
        super().__init__()  
        #Pin Rows
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
        # Pin Columns
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

#---------------------------------------------------------------------#

class Board2(LedMatrix):
    def __init__(self):
        super().__init__()  
        #Pin Rows
        self.PIN_ROWS = {
            1: digitalio.DigitalInOut(board.D6),
            2: digitalio.DigitalInOut(board.D2),
            3: digitalio.DigitalInOut(board.D5),
            4: digitalio.DigitalInOut(board.D1),
            5: digitalio.DigitalInOut(board.D5),
            6: digitalio.DigitalInOut(board.D0),
            7: digitalio.DigitalInOut(board.D3),
            8: digitalio.DigitalInOut(board.SCL)
            }
        # Pin Columns
        self.PIN_COLUMNS = {
            1: digitalio.DigitalInOut(board.A3),  
            2: digitalio.DigitalInOut(board.A4),
            3: digitalio.DigitalInOut(board.A5),
            4: digitalio.DigitalInOut(board.MOSI),
            5: digitalio.DigitalInOut(board.MISO),
            6: digitalio.DigitalInOut(board.RX),
            7: digitalio.DigitalInOut(board.TX),
            8: digitalio.DigitalInOut(board.D2)
            }
        # configure each pin as output
        for pin in self.PIN_ROWS.values():
            pin.direction = digitalio.Direction.OUTPUT

        for pin in self.PIN_COLUMNS.values():
            pin.direction = digitalio.Direction.OUTPUT
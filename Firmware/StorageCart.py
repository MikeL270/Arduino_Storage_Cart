# Library used to control an 8x8 LED matrix
# Written by Michael Lance
# Created: 5/16/2024
# Last Modified: 6/04/2024
#---------------------------------------------------------------------#
"""
        commands are strings with a predefined structure
        commands structured as such: [command_type][arg]
        ex: 1 == turn on all leds
        ex 2: 2 1x1 == turn on led at row 1, column 1
"""
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
        
        
        # Initialize command handlers
        self.command_handlers = {
            "0": self.all_off,
            "1": self.all_on,
            "2": self.led_on,
        }
        
    def led_on(self, grid_coordinate):
        column = grid_coordinate[0]
        row = grid_coordinate[2]
        
        # Turn off all LEDs first
        self.all_off()
        
        # Turn on the selected power pin to true
        self.PIN_COLUMNS[column].value = False

        # Set the selected ground pin to false
        self.PIN_ROWS[row].value = True

    def all_on(self, arg=None):
        for pin in self.PIN_ROWS.values():
            pin.value = True

        for pin in self.PIN_COLUMNS.values():
            pin.value = False

    def all_off(self, arg=None):
        for pin in self.PIN_ROWS.values():
            pin.value = False

        for pin in self.PIN_COLUMNS.values():
            pin.value = True

    def decode_command(self, message):
        command_type = message[0:1]
        arg = message[2:] if len(message) > 2 else None

        handler = self.command_handlers.get(command_type)
        if handler:
            handler(arg)
        else:
            print("Error: Unknown command type.")

#---------------------------------------------------------------------#

class Board1(LedMatrix):
    def __init__(self):
        super().__init__()  
        #Pin Rows
        self.PIN_ROWS = {
            "1": digitalio.DigitalInOut(board.MISO),
            "2": digitalio.DigitalInOut(board.A0),
            "3": digitalio.DigitalInOut(board.RX),
            "4": digitalio.DigitalInOut(board.A1),
            "5": digitalio.DigitalInOut(board.TX),
            "6": digitalio.DigitalInOut(board.A2),
            "7": digitalio.DigitalInOut(board.SDA),
            "8": digitalio.DigitalInOut(board.A3)
            }
        # Pin Columns
        self.PIN_COLUMNS = {
            "1": digitalio.DigitalInOut(board.MOSI),  
            "2": digitalio.DigitalInOut(board.A5),
            "3": digitalio.DigitalInOut(board.SCK),
            "4": digitalio.DigitalInOut(board.A4),
            "5": digitalio.DigitalInOut(board.D2),
            "6": digitalio.DigitalInOut(board.D5),
            "7": digitalio.DigitalInOut(board.D6),
            "8": digitalio.DigitalInOut(board.SCL)
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
            1: digitalio.DigitalInOut(board.D13),
            2: digitalio.DigitalInOut(board.D9),
            3: digitalio.DigitalInOut(board.D12),
            4: digitalio.DigitalInOut(board.D6),
            5: digitalio.DigitalInOut(board.D11),
            6: digitalio.DigitalInOut(board.D5),
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
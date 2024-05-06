# Libraries used to interact with the Adafruit NRF52840 Express
import board
import digitalio
import time

#---------------------------------------------------------------------#
# Classes

class LedMatrix:
    def __init__(self):

        # Pin Rows
        PIN_ROWS = {
        "PIN_ROW_1": digitalio.DigitalInOut(board.D2),
        "PIN_ROW_2": digitalio.DigitalInOut(board.TX),
        "PIN_ROW_3": digitalio.DigitalInOut(board.RX),
        "PIN_ROW_4": digitalio.DigitalInOut(board.MISO),
        "PIN_ROW_5": digitalio.DigitalInOut(board.MOSI),
        "PIN_ROW_6": digitalio.DigitalInOut(board.SCK),
        "PIN_ROW_7": digitalio.DigitalInOut(board.A5),
        "PIN_ROW_8": digitalio.DigitalInOut(board.A4)
        }

        # Pin COLUMNs
        PIN_COLUMNS = {
        "PIN_COLUMN_1": digitalio.DigitalInOut(board.SDA),  
        "PIN_COLUMN_2": digitalio.DigitalInOut(board.SLC),
        "PIN_COLUMN_3": digitalio.DigitalInOut(board.D5),
        "PIN_COLUMN_4": digitalio.DigitalInOut(board.D6),
        "PIN_COLUMN_5": digitalio.DigitalInOut(board.D9),
        "PIN_COLUMN_6": digitalio.DigitalInOut(board.D10),
        "PIN_COLUMN_7": digitalio.DigitalInOut(board.D11),
        "PIN_COLUMN_8": digitalio.DigitalInOut(board.D12)
        }

        self.rowModes = []
        self.columnModes = []

        # configure each pin as output
        for pin in self.PIN_ROWS.values():
            pin.direction = digitalio.Direction.OUTPUT

        for pin in self.PIN_COLUMNS.values():
            pin.direction = digitalio.Direction.OUTPUT

    def turnOnLed(self, row, COLUMN):

        # Set all pins off first
        for pin in self.PIN_ROWS.values():
            pin.value = False

        for pin in self.PIN_COLUMNS.values():
            pin.value = True

        # Turn on the selected row
        self.PIN_ROWS[selected_row].value = True

        # Turn off the selected column
        self.PIN_COLUMNS[selected_column].value = False  

"""
class LedMatrix:
    def __init__(self, pin1, pin2, pin3, pin4):
        self.ROW_ONE_SOL_GR_BR = digitalio.DigitalInOut(board.pin1)
        self.ROW_ONE_SOL_BL_OR = digitalio.DigitalInOut(board.pin2)
        self.ROW_ONE_STR_GR_BL = digitalio.DigitalInOut(board.pin3)
        self.ROW_ONE_STR_BR_OR =  digitalio.DigitalInOut(board.pin4)
        
        self.ROW_ONE_SOL_GR_BR.direction = digitalio.Direction.OUTPUT
        self.ROW_ONE_SOL_BL_OR.direction = digitalio.Direction.OUTPUT
        self.ROW_ONE_STR_GR_BL.direction = digitalio.Direction.OUTPUT
        self.ROW_ONE_STR_BR_OR.direction = digitalio.Direction.OUTPUT
        
        self.ledOnConfig = [
            (False, False, False, False),# None On Default
            (True, False, False, True),  # Green On
            (False, True, True, False),  # Orange On
            (False, True, False, True),  # Blue On
            (True, False, True, False),  # Brown On
        ]

    def turnOnLed(self, ledId):
        self.ROW_ONE_SOL_GR_BR.value = self.ledOnConfig[ledId][0]
        self.ROW_ONE_SOL_BL_OR.value = self.ledOnConfig[ledId][1]
        self.ROW_ONE_STR_GR_BL.value = self.ledOnConfig[ledId][2]
        self.ROW_ONE_STR_BR_OR.value = self.ledOnConfig[ledId][3]

#---------------------------------------------------------------------#
# Instancing objects 4 lights n stuff

RowOne = LedMatrix(FIRST_GROUP)

"""
#---------------------------------------------------------------------#
# Run ad infinitum (and beyond)

while True:

    

    """
    RowOne.turnOnLed(GREEN_LED)
    print("Turing first row led solid green on")
    time.sleep(1)
    RowOne.turnOnLed(ORANGE_LED)
    print("orange!")
    time.sleep(1)
    RowOne.turnOnLed(BLUE_LED)
    print("blue!")
    time.sleep(1)
    """


"""
# Create a digital input/output pin on D13
led = digitalio.DigitalInOut(board.D13)
led.direction = digitalio.Direction.OUTPUT

while True:
    # Turn the LED on
    led.value = True
    # Print a message to the serial console
    print("wizard 101")
    # Wait for 1 second
    time.sleep(1)
    # Turn the LED off
    led.value = False
    # Wait for another second
    time.sleep(1)

"""
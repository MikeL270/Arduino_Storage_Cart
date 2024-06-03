# Storage cart testing firmware 
# Written by Michael Lance
# 5/16/2024
# Updated: 5/23/2024
#---------------------------------------------------------------------#
import StorageCart
import communications
import time

test = communications.CommAgent()
board = StorageCart.Board1()

print("running")
while True:
    message = test.return_payload().decode('utf-8')

    board.led_on(message[0], message[2])

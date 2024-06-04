# Storage cart testing firmware 
# Written by Michael Lance
# 5/16/2024
# Updated: 6/04/2024
#---------------------------------------------------------------------#
import StorageCart
import communications
import time

test = communications.CommAgent()
board = StorageCart.Board1()
 
print("running")
while True:
    message = test.return_payload().decode('utf-8')
    board.decode_command(message)
    

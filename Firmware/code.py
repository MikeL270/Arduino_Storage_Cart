# Storage cart testing firmware 
# Written by Michael Lance
# 5/16/2024
# Updated: 5/16/2024
#---------------------------------------------------------------------#
from StorageCart import LedMatrix

test_cart = LedMatrix()

while True:
    led_row = int(input())
    led_collumn = int(input())
    
    test_cart.led_on(led_row, led_collumn)
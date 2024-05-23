# Storage cart testing firmware 
# Written by Michael Lance
# 5/16/2024
# Updated: 5/23/2024
#---------------------------------------------------------------------#
import StorageCart

test_cart = StorageCart.Board1()

while True:
    led_row = int(input())
    led_collumn = int(input())
    
    test_cart.led_on(led_row, led_collumn)
from pyfirmata import Arduino, util
import time
board = Arduino('COM5') #Here you need write your 'COM' Port number
board.digital[12].write(1)
time.sleep(3.0)
board.digital[12].write(0)
time.sleep(3.0)
board.digital[12].write(1)
time.sleep(3.0)
board.digital[12].write(0)

print("Comming to the for loop")

for i in range(5):
    board.digital[12].write(1)
    time.sleep(3.0)
    board.digital[12].write(0)
    time.sleep(3.0)
    
print("Now the led will glow infinity time")

while True:
    board.digital[12].write(1)
    time.sleep(1.0)
    board.digital[12].write(0)
    time.sleep(1.0)
    
    
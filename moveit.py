from pynput import mouse, keyboard
import time
from datetime import datetime


button = mouse.Button
mouse = mouse.Controller()

# I might add keyboard interaction. But here it is for now
# key = keyboard.Key
# keyboard = keyboard.Controller()



count = 0 # to count how many times action is done!

print('\n\nWelcome to MoveIt app!\n')

def moveIt():
    global count
    count = count + 1

    # Get time
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")

    currentPos = mouse.position # save current position of mouse!
    mouse.position = (2, 700) # move it to the left of the screen somewhere in the middle!

    time.sleep(0.1) # Wait a bit...
    mouse.move(5, 5)

    time.sleep(0.1) # Wait again...
    mouse.click(button.right, 1) # make a right click!

    time.sleep(0.05) # Wait again...
    mouse.position = (700, 1000)
    mouse.click(button.left, 1) # make a click!

    time.sleep(0.1) # Wait...
    mouse.position = (int(currentPos[0]), int(currentPos[1])) #move mouse back to where it was!
    # print("Count:", count, "Mouse moved at:", current_time)

    # # Keyboard action
    # time.sleep(0.1)
    # with keyboard.pressed(key.cmd):
    #     keyboard.press(key.tab)

    # wait before click again...
    time.sleep(120)

while True:
    moveIt()

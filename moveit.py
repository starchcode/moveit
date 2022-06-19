from pynput import mouse, keyboard
import time
from datetime import datetime


button = mouse.Button
mouseController = mouse.Controller()

# I might add keyboard interaction. But here it is for now
# key = keyboard.Key
# keyboard = keyboard.Controller()

count = 0 # to count how many times action is done!
shouldMove = True

def on_move(x, y):
    global shouldMove
    shouldMove = False


listener = mouse.Listener(on_move=on_move)
listener.start()




print('\n\nWelcome to MoveIt app!\n')

def moveIt():
    global count
    global shouldMove
    count = count + 1

    # Get time
    # now = datetime.now()
    # current_time = now.strftime("%H:%M:%S")


    if shouldMove:
        currentPos = mouseController.position # save current position of mouseController!
        mouseController.position = (2, 700) # move it to the left of the screen somewhere in the middle!

        time.sleep(0.1) # Wait a bit...
        mouseController.move(5, 5)

        time.sleep(0.1) # Wait again...
        mouseController.click(button.right, 1) # make a right click!

        time.sleep(0.05) # Wait again...
        mouseController.position = (700, 1000)
        mouseController.click(button.left, 1) # make a click!

        time.sleep(0.1) # Wait...
        mouseController.position = (int(currentPos[0]), int(currentPos[1])) #move mouse back to where it was!
        # print("Count:", count, "Mouse moved at:", current_time)

        # # Keyboard action
        # time.sleep(0.1)
        # with keyboard.pressed(key.cmd):
        #     keyboard.press(key.tab)

        # wait before click again...
    else:
        shouldMove = True

    time.sleep(60) # value times 2 will be the wait before clicks. so 60 would mean 120

while True:
    moveIt()

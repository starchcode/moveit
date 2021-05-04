from pynput import mouse, keyboard
import time
from datetime import datetime


button = mouse.Button
mouse = mouse.Controller()

key = keyboard.Key
keyboard = keyboard.Controller()



count = 0

print('\n\nWelcome to MoveIt app!\n')
def executeSomething():
    global count
    count = count + 1
    # Get time
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    currentPos = mouse.position
    mouse.position = (2, 700)
    time.sleep(0.1)
    mouse.move(5, 5)
    # time.sleep(1)
    time.sleep(0.1)
    mouse.click(button.right, 1)

    time.sleep(0.1)
    mouse.position = (int(currentPos[0]), int(currentPos[1]))
    print("Count:", count, "Mouse moved at:", current_time)

    # # Keyboard action
    # time.sleep(0.1)
    # with keyboard.pressed(key.cmd):
    #     keyboard.press(key.tab)

    # wait before click again...
    time.sleep(120)

while True:
    executeSomething()

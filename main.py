import pyautogui
import time
import keyboard

# Set the target coordinates for clicking
x = 500
y = 500

# Set the desired interval between clicks in seconds
click_interval = 1

# Set the number of clicks you want to perform
num_clicks = 10

# Set the key to stop the clicking process
stop_key = "q"

# Pause for a few seconds to allow you to position the mouse cursor
print("Move your mouse to the desired clicking position...")
time.sleep(5)

# Perform the clicks
print("Press '{}' to stop the clicking process.".format(stop_key))
for _ in range(num_clicks):
    pyautogui.click(x, y)
    time.sleep(click_interval)
    
    # Check if the stop key is pressed
    if keyboard.is_pressed(stop_key):
        print("Clicking process stopped.")
        break

print("Clicking completed.")

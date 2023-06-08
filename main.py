import pyautogui
import time

# Set the target coordinates for clicking
x = 500
y = 500

# Set the desired interval between clicks in seconds
click_interval = 1

# Set the number of clicks you want to perform
num_clicks = 10

# Pause for a few seconds to allow you to position the mouse cursor
print("Move your mouse to the desired clicking position...")
time.sleep(5)

# Perform the clicks
for _ in range(num_clicks):
    pyautogui.click(x, y)
    time.sleep(click_interval)

print("Clicking completed.")

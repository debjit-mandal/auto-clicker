import pyautogui
import time
import random
import keyboard

# Define the target coordinates for clicking
click_positions = [(500, 500), (600, 600), (700, 700)]

# Set the minimum and maximum delay between clicks in seconds
min_delay = 0.5
max_delay = 2.0

# Set the key to stop the clicking process
stop_key = "q"

# Pause for a few seconds to allow you to position the mouse cursor
print("Move your mouse to the desired clicking positions...")
time.sleep(5)

# Perform the clicks
print("Press '{}' to stop the clicking process.".format(stop_key))
try:
    while True:
        for position in click_positions:
            pyautogui.click(position[0], position[1])

            # Generate a random delay between clicks
            delay = random.uniform(min_delay, max_delay)
            time.sleep(delay)

            # Check if the stop key is pressed
            if keyboard.is_pressed(stop_key):
                print("Clicking process stopped.")
                raise KeyboardInterrupt

except KeyboardInterrupt:
    print("Clicking process interrupted.")

print("Clicking completed.")

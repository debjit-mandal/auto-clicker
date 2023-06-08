import pyautogui
import time
import keyboard

# Define the target coordinates for clicking
click_positions = [(500, 500), (600, 600), (700, 700)]

# Set the desired interval between clicks in seconds
click_interval = 1

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
            time.sleep(click_interval)

            # Check if the stop key is pressed
            if keyboard.is_pressed(stop_key):
                print("Clicking process stopped.")
                raise KeyboardInterrupt

except KeyboardInterrupt:
    print("Clicking process interrupted.")

print("Clicking completed.")

import pyautogui
import time
import random
import keyboard

# List to store the recorded click positions
click_positions = []

# Set the minimum and maximum delay between clicks in seconds
min_delay = 0.5
max_delay = 2.0

# Set the key to stop the clicking process
stop_key = "q"
record_key = "r"

# Set the duration of the clicking process in seconds
click_duration = 10

# Pause for a few seconds to allow you to position the mouse cursor
print("Move your mouse to the desired clicking positions...")
time.sleep(5)

# Record click positions
print("Press '{}' to record the current mouse position.".format(record_key))
print("Press '{}' to stop recording.".format(stop_key))
while True:
    if keyboard.is_pressed(record_key):
        click_positions.append(pyautogui.position())
        time.sleep(0.2)
    if keyboard.is_pressed(stop_key):
        break

# Perform the clicks
print("Press '{}' to stop the clicking process.".format(stop_key))
start_time = time.time()
try:
    while time.time() - start_time < click_duration:
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

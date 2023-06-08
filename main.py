import pyautogui
import time
import random
import keyboard

# List to store the recorded click positions and drag path
click_positions = []
drag_path = []

# Set the minimum and maximum delay between clicks in seconds
min_delay = 0.5
max_delay = 2.0

# Set the key to stop the clicking process
stop_key = "q"
record_key = "r"
drag_key = "d"
duration_increase_key = "+"
duration_decrease_key = "-"

# Set the initial click interval
click_interval = 1.0

# Set the initial drag duration in seconds
drag_duration = 0.5

# Set the initial click duration in seconds
click_duration = 10

# Pause for a few seconds to allow you to position the mouse cursor
print("Move your mouse to the desired clicking positions...")
time.sleep(5)

# Record click positions and drag path
print("Press '{}' to record the current mouse position.".format(record_key))
print("Press '{}' to record the drag path.".format(drag_key))
print("Press '{}' to stop recording.".format(stop_key))

recording_drag = False

while True:
    if keyboard.is_pressed(record_key):
        click_positions.append(pyautogui.position())
        time.sleep(0.2)
    elif keyboard.is_pressed(drag_key):
        recording_drag = True
        print("Recording drag path...")
        time.sleep(0.2)
    elif recording_drag and pyautogui.position() not in drag_path:
        drag_path.append(pyautogui.position())
        time.sleep(0.1)
    elif keyboard.is_pressed(stop_key):
        break

# Perform the clicks and drag
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

        if drag_path:
            pyautogui.dragTo(
                drag_path[-1][0], drag_path[-1][1], duration=drag_duration
            )

        # Check if interval adjustment keys are pressed
        if keyboard.is_pressed(duration_increase_key):
            drag_duration += 0.1
            print("Drag duration increased to:", drag_duration)
        elif keyboard.is_pressed(duration_decrease_key):
            drag_duration -= 0.1
            if drag_duration < 0.1:
                drag_duration = 0.1
            print("Drag duration decreased to:", drag_duration)

        time.sleep(0.1)  # Small delay between checks

except KeyboardInterrupt:
    print("Clicking process interrupted.")

print("Clicking completed.")

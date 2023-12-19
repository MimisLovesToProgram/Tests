from pynput import keyboard

word = ""

def on_press(key):
    global word
    if key != keyboard.Key.enter and key != keyboard.Key.shift and key != keyboard.Key.caps_lock and key != keyboard.Key.space:
        word += key.char
    elif key == keyboard.Key.space:
        word += " "

def on_release(key):
    if key == keyboard.Key.enter:
        # Stop listener
        return False

# Collect events until released
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

print(word)

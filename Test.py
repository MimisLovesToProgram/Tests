import tkinter as tk
from tkinter import ttk

# Create the main window
root = tk.Tk()
root.title("Simple GUI")

# Create a Text
label_text = tk.StringVar()
text = ttk.Label(root, textvariable=label_text)
text.pack(padx=0, pady=0)

times = 0

def on_button_click():
    global times
    times += 1
    label_text.set(f"Button Clicked {times} times")

# Create a button
button = ttk.Button(root, text="Click me!", command=on_button_click)
button.pack(padx=100, pady=100)

# Start the Tkinter event loop
root.mainloop()

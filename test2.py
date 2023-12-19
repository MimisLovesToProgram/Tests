import pyautogui
import random

while True:
    posx = random.randrange(0, pyautogui.size().width + 1)
    posy = random.randrange(0, pyautogui.size().height + 1)
    pyautogui.moveTo(posx, posy, .25)

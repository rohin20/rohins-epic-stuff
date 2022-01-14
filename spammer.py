import pyautogui
import time
time.sleep(5)

file = open('movie', 'r', encoding="utf8")

for word in file:
    time.sleep(0.3)
    pyautogui.typewrite(word)
    pyautogui.press('enter')

    

















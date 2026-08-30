import pyautogui
import time

pyautogui.PAUSE = 1.0

# Step 1: Open Run (Win+R)
pyautogui.hotkey("win", "r")
time.sleep(2)

# Step 2: Type "notepad" and press Enter
pyautogui.typewrite("notepad", interval=0.1)
pyautogui.press("enter")
time.sleep(2)

# Step 3: Type your message in Notepad
pyautogui.typewrite("Do you see anything getting typed here.?\n", interval=0.1)
time.sleep(1)
pyautogui.typewrite("Its not your pyautogui. I’m a\n", interval=0.1)
time.sleep(1)

# Step 3b: Continue typing
pyautogui.typewrite("PEI\n", interval=0.1)
pyautogui.typewrite("Wanna see me??\n", interval=0.1)
time.sleep(2)

# Step 4: Open Start menu (Win key)
pyautogui.press("win")
time.sleep(1)

# Step 5: Type "edge" and press Enter
pyautogui.typewrite("edge", interval=0.1)
pyautogui.press("enter")
time.sleep(3)

# Step 6: Type search phrase in Edge
pyautogui.typewrite("ghost sitting in the dark images", interval=0.1)
pyautogui.press("enter")

# Step 7: Zoom the browser
pyautogui.hotkey("ctrl", "+")
pyautogui.hotkey("ctrl", "+")
pyautogui.hotkey("ctrl", "+")

# Step 8: Scroll down the page
for _ in range(3):
    pyautogui.scroll(-500)
    time.sleep(1)
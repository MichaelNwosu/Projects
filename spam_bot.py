import pyautogui
import time

f=input("Enter :")

def spam():
    while True:
        
        for word in f:
            pyautogui.typewrite(f)
            time.sleep(0.001)
            pyautogui.press("enter")

spam()
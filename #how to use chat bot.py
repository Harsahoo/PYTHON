#how to use chat bot

import webbrowser
import pyautogui
import time

person_name = input('Enter The Person Name Whom You Want To Send A Message: ')
#my_msg = input('Enter Your Message: ')

webbrowser.open("https://www.linkedin.com/feed/")
time.sleep(8)

#print(pyautogui.position())

pyautogui.click(119,172)
pyautogui.typewrite(person_name)

time.sleep(5)
pyautogui.click(172,228)


pyautogui.dragTo(100, 200, button='left')     # drag mouse to X of 100, Y of 200 while holding down left mouse button
pyautogui.dragTo(300, 400, 2, button='left')  # drag mouse to X of


pyautogui.scroll(10)   # scroll up 10 "clicks"
time.sleep(5)

print(pyautogui.position())

#pyautogui.click(172,228)   
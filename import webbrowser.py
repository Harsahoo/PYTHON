import webbrowser
import pyautogui
import time
harsh= print(input("kya nam dalna hai"))
webbrowser.open("https://paint.js.org/")
print(pyautogui.size())
time.sleep(5)

for i in range(10):
      pyautogui.dragTo(400, 300,  button='left')
      time.sleep(2)
      pyautogui.dragTo(500, 500, button='left')
      time.sleep(2)
      pyautogui.dragTo(200, 200, button='left')
      time.sleep(2)
      pyautogui.dragTo(300, 200, button='left')

time.sleep(8)
 #save file 
print(pyautogui.position())
pyautogui.click(16,147)   
pyautogui.click(64,219)
time.sleep(1)

pyautogui.click(172,635)
pyautogui.typewrite(harsh)

for i in range(3): 
   pyautogui.click(1203,703) 
   time.sleep(1)
   pyautogui.click(1203,703)       
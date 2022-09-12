#insta bot made by harsh sahu

import pyautogui,time, webbrowser

#webbrowser.open(url="")
story=int(input('how many stroies'))
post= int(input('how many post you want to like '))
foll=int(input('how many followers'))

q=int(input('enter the no of girl you want to be friend'))
name=input('enter the name of girl you want to be friend')


webbrowser.open(url="https://www.instagram.com/")

time.sleep(3)
print(pyautogui.position())

#for opening story section 
time.sleep(5)
pyautogui.click(x=246, y=326)
pyautogui.click(x=292, y=291)
time.sleep(2)
#for likikg stories
for i in range(story):

     time.sleep(2)
     pyautogui.click(x=800, y=672)
     time.sleep(2)
     pyautogui.press('right')
     time.sleep(8)


#for closing stories
pyautogui.click(x=1298, y=183)
time.sleep(2)


#for scrolling to new posts
#pyautogui.mouseInfo()
for p in range (post):
    pyautogui.moveTo(559,480)
    for s in range (20):
         pyautogui.scroll(-20)
         time.sleep(0.5)
     
     
    pyautogui.click(529,430)
    pyautogui.press('tab')
    pyautogui.press('space')
    pyautogui.click(160,170)
    pyautogui.press('F5')
    time.sleep(8)
    

for i in range (foll):
    pyautogui.click(1127,414)
    time.sleep(2)
    pyautogui.click(1127,470)
    time.sleep(2)
    pyautogui.click(1127,528)
    time.sleep(2)
    pyautogui.click(1127,585)
    time.sleep(2)
    pyautogui.click(1127,642)
    time.sleep(2)
    pyautogui.click(160,170)
    pyautogui.press('F5')
    time.sleep(8)







#new friend script

pyautogui.click(160,170)
time.sleep(2)
  


for i in range(q):
    time.sleep(5)
    pyautogui.moveTo(583,174)
    time.sleep(2)
    pyautogui.click(583,174)

    pyautogui.typewrite(name)   #write name in search bar(need to add a function which every time gives new name )

    time.sleep(5)
    pyautogui.moveTo(588,387)
    time.sleep(2)
    for s in range (2):
        pyautogui.scroll(-20)
        time.sleep(0.5)
    pyautogui.click(583,387)

    time.sleep(5)
    pyautogui.click(700,340)
    time.sleep(2)
    pyautogui.click(815,364)
    time.sleep(2)
    pyautogui.click(812,434)
    time.sleep(2)
    pyautogui.click(812,521)
    time.sleep(2)
    pyautogui.click(884,315)
    time.sleep(2)   


    time.sleep(3)
    pyautogui.moveTo(588,387)
    time.sleep(2)
    for s in range (20):
        pyautogui.scroll(-200)
        time.sleep(0.5)
        pyautogui.scroll(100)
        time.sleep(0.5)
    pyautogui.click(160,170)
    
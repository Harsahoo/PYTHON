#new people finder


import pyautogui 
import time 
import webbrowser 

"""man=int(input('input do for interval'))
x =int(input('input do for x'))
y=1000"""
"""webbrowser.open('https://www.instagram.com/')
while(x < y):
    x=x+man
    y=x+200
    
    
    print(x,y)

    c= pyautogui.position(x,y)

    time.sleep(1)
    print(c)
    time.sleep(4)
    pyautogui.click(c)"""


# automating messages
#x =['pooja' , 'karishma' , 'aarti']
#y =['sahu' , 'sharma' , 'agarwal']
"""
#new freind 
pyautogui.click()
# number of elements as input
n = int(input("Enter number of elements : "))
  
# iterating till the range
for i in range(0, n):
    ele = int(input())
  
    lst.append(ele) # adding the element
      
print(lst)

"""
#pyautogui.displayMousePosition()

# pyautogui.mouseInfo()

"""name=[]
n=int(input('enter the no of girls you want to search' ))
# iterating till the range
for i in range(0, n):
    ele = str(input())
  
    name.append(ele) # adding the element
      
    print(name)"""



#code start
q=int(input('enter the no of girl you want to be friend'))
name=input('enter the name of girl you want to be friend')
webbrowser.open('https://www.instagram.com/')


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
#jaffer razavi
#oct 25, 2019


import pyautogui
import webbrowser
import time

message = input("What message do you want to keep sending? \n ")
repeats = int(input("How many times do you want to send the message?  \n"))
delay = int(input("How many seconds do you want to wait in between each message?  \n"))

isLoaded = input("Press Enter when your messaging app is loaded up. \n")



print("You have five seconds to focus the text input area \n")

time.sleep(5)


for i in range(0,repeats):         #Message sending loop
	if message != "":
		pyautogui.typewrite(message)     
		pyautogui.press("enter")
	else:
		pyautogui.hotkey('ctrl', 'v')      
		pyautogui.press("enter")

	time.sleep(delay)


print("Done\n")

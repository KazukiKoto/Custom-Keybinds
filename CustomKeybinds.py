import keyboard
import os
import time
import pyautogui
from cryptography.fernet import Fernet

############################## Login Function

def FFxivLogin():
    isLocated=None
    while True:
        try:
            isLocated = pyautogui.locateOnScreen("F:\\CustomKeybinds\\FFxiv_Login.png", confidence=0.9) #Looks for login prompt on screen
            if isLocated!=None:
                break #Break infinite loop
        except:
            isLocated=None
    time.sleep(2)
    pyautogui.leftClick(x=1414,y=701) #Position of password box
    file = open("CHANGE DRIVE HERE:\\CHANGE FILEPATH HERE\\FFPW.txt","r") #Retrieves encrypted password from filepath CHANGE FILEPATH FOR PERSONAL PW
    encryptedPW=file.read() #Saves to variable
    file = open("CHANGE DRIVE HERE:\\CHANGE FILEPATH HERE\\Key.txt","r") #Retrieves encryption key from filepath CHANGE FILEPATH FOR PERSONAL KEY
    key=file.read() #Saves to variable
    f=Fernet(key)
    decryptedPW = f.decrypt(encryptedPW) #Decrypts PW
    PW=(str(decryptedPW).replace("b'","")).replace("'","") #Formats for typing into Password box
    pyautogui.write(PW)
    pyautogui.press("enter") #Enters Password
    isLocated=None
    while True:
        try:
            isLocated = pyautogui.locateOnScreen("CHANGE DRIVE HERE:\\CHANGE FILEPATH HERE\\FFxiv_Login2.png", confidence=0.9) #Searches for Login Button
            if isLocated!=None:
                break
        except:
            isLocated=None
    pyautogui.leftClick(x=1513,y=826) #Clicks Login

############################ MAIN CODE

while True:
    if keyboard.is_pressed("shift+ctrl+f8"): #This keybind runs and logs into FFxiv
        filepath="C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\SQUARE ENIX\\FINAL FANTASY XIV ONLINE\\FINAL FANTASY XIV.lnk" #File path to application FILEPATH SHOULD BE CONSISTENT IF NOT FIND YOUR FILEPATH
        os.startfile(filepath) #Opens FFxiv
        FFxivLogin() #Seperate function to login
    time.sleep(0.1)
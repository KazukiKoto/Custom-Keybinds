import keyboard
import os
import time
import pyautogui
from cryptography.fernet import Fernet
import tkinter
from pynput import keyboard as kb
from pynput.keyboard import Key

############################## Tkinter

def Keybinds_GUI():
    global root
    root= tkinter.Tk()
    root.geometry("1000x1000+100+100")
    
    TitleLabel=tkinter.Label(root, text="Keybinds:", font=("Helvetical bold",40))
    TitleLabel.grid(row=0)
    FinalFantasyButton=tkinter.Button(root, text="Boot FFxiv", command=lambda:[FFxivLogin()])
    FinalFantasyButton.grid(row=1,column=0)
    MacroLibraryButton=tkinter.Button(root, text="Macro Library", command=lambda:[Macro_Library_GUI()])
    MacroLibraryButton.grid(row=2,column=0)
    
    root.mainloop()

def Macro_Library_GUI():
    root.destroy()
    global macro
    macro= tkinter.Tk()
    macro.geometry("1000x1000+100+100")
    
    TitleLabel=tkinter.Label(macro, text="Macro Library:", font=("Helvetical bold",40))
    TitleLabel.grid(row=0,column=0)
    ListenButton=tkinter.Button(macro, text="Listen", command=lambda:[Macro_Library_Listen()])
    ListenButton.grid(row=1,column=0)
    PlayButton=tkinter.Button(macro, text="Play", command=lambda:[Play_GUI()])
    PlayButton.grid(row=2,column=0)
    
    BackButton=tkinter.Button(macro, text="Back", command=lambda:[macro.destroy(),Keybinds_GUI()])
    BackButton.grid(row=0, column=2)  
    
    macro.mainloop()

def Play_GUI():
    macro.destroy()
    global play
    play=tkinter.Tk()
    play.geometry("1000x1000+100+100")
    
    TitleLabel=tkinter.Label(play, text="Existing Macros:", font=("Helvetical bold",40))
    TitleLabel.grid(row=0,column=0)
    
    
    BackButton=tkinter.Button(play, text="Back", command=lambda:[play.destroy(),Macro_Library_GUI()])
    BackButton.grid(row=0, column=2)    
    play.mainloop()

############################## Login Function

def On_Press(key):
    try:
        print(key.char)
    except:
        print(key)
def Macro_Library_Listen():
    print("Listening")
    with kb.Listener(On_Press=On_Press) as Listener:
        Listener.join()
    


def FFxivLogin():
    filepath="C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\SQUARE ENIX\\FINAL FANTASY XIV ONLINE\\FINAL FANTASY XIV.lnk" #File path to application FILEPATH SHOULD BE CONSISTENT IF NOT FIND YOUR FILEPATH
    os.startfile(filepath) #Opens FFxiv
    isLocated=None
    while True:
        try:
            isLocated = pyautogui.locateOnScreen("CHANGE DRIVE HERE:\\CHANGE FILEPATH HERE\\FFxiv_Login.png", confidence=0.9) #Looks for login prompt on screen
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
        Keybinds_GUI()
    time.sleep(0.1)
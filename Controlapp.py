import os 
import pyautogui
import webbrowser
import pyttsx3
from time import sleep

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(text, rate = 145):
    engine.setProperty('rate',rate)
    engine.say(text)
    engine.runAndWait()
    
controlapp = {"commandprompt":"cmd","paint":"paint","word":"winword","excel":"excel","chrome":"chrome","vscode":"code","powerpoint":"powerpnt","brave":"brave"}

def openappweb(query):
    speak("Im Launching the app sir") # opening apps
    if ".com" in query or ".co.in" in query or ".org" in query:
        query = query.replace("open","")
        query = query.replace("athena","")  # not working logical call out error???
        query = query.replace("launch","")  # unable to open and close web tabs 
        query = query.replace(" ","")
        webbrowser.open(f"https://wwww.{query}")
    else:
        keys = list(controlapp.keys())
        for app in keys:
            if app in query:
                os.system(f"start {controlapp[app]}")
                
                
def closeappweb(query):
    speak("Alright sir, Closing it")
    if "one tab" in query or "1 tab" in query:
        pyautogui.hotkey("ctrl","w")
    elif "2 tab" in query:
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)                       # not working logical error 
        pyautogui.hotkey("ctrl","w")
        speak("All tabs are closed sir")
    elif "3 tab" in query:
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        speak("All tabs are closed sir")
    elif "4 tab" in query:
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        speak("All tabs are closed sir")
    elif "5 tab" in query:
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        speak("All tabs are closed sir")
        
    #if u want to add more tabs 
    else:
        keys = list(controlapp.keys())   # close apps 
        for app in keys:
            if app in query:
                os.system(f"taskkill /f /im {controlapp[app]}.exe")
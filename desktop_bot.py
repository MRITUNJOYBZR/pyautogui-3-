import pyautogui
import time
import os
import subprocess
import platform

def open_application(app_name):
    system = platform.system()

    '''Using the OS library, we detect what operating system we are working on
    if it is windows, a subprocess is made in the command prompt, if it is Darwin/ MacOS, a new 
    sub process is made in the terminal or if it is linux, a new subprocess is made in the terminal'''
    
    
    if system == "Windows":
        subprocess.Popen(app_name)
    elif system == "Darwin":  
        subprocess.Popen(["open", "-a", app_name])
    elif system == "Linux":
        subprocess.Popen([app_name])
    else:
        # The code is yet designed to detect only 3 types of OS
        print("Unsupported OS")

def type_text(text, delay=0.1):

    '''Function to type text automatically:
    - Waits 2 seconds to allow the app to come into focus and to allow the user to change tabs if necessary
    - Types the provided text with a small delay between characters'''

    time.sleep(2)  
    pyautogui.write(text, interval=delay)

def click_position(x, y):

    '''Function to simulate a mouse click at a specific screen position:
    - Takes (x, y) coordinates as input
    - Moves the mouse to that position and clicks'''

    pyautogui.click(x=x, y=y)

def rename_file(old_path, new_path):

    '''Function to rename a file:
    - Checks if the original file exists
    - If it does, renames it to the new name
    - Otherwise, prints a file-not-found message'''

    if os.path.exists(old_path):
        os.rename(old_path, new_path)
        print(f"Renamed: {old_path} → {new_path}")
    else:
        print("File not found.")

if __name__ == "__main__":
    print("Opening Notepad...")
    open_application("notepad.exe")
    time.sleep(2)
    type_text("Hello from PyAutomate AI")

'''Notepad is just a demo in this code, we can open any kind of application or even URL if 
we want to.'''

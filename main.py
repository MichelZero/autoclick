import time
import threading
from pynput.mouse import Button, Controller
from pynput.keyboard import Key, Listener, KeyCode


ToggleKey = KeyCode(char='t')

clicking = False
mouse = Controller()

def clicker():
    while clicking:
        mouse.click(Button.left)
        time.sleep(0.001)
        
def toggle_event(key):
    global clicking
    if key == ToggleKey:
        if clicking:
            clicking = False
        else:
            clicking = True
          
clicker_thread = threading.Thread(target=clicker)
clicker_thread.start()

with Listener(on_press=toggle_event) as listener:
    listener.join()
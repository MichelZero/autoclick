import time
import threading
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode
from playsound import playsound as playsom

tecla = KeyCode(char="t") # tecla que vai ser usada para ativar o clicker
clicking = False        # variavel que vai ser usada para saber se o clicker esta ativo ou nao
mouse = Controller()   # variavel que vai ser usada para controlar o mouse
som = "som.mp3"        # variavel que vai ser usada para armazenar o caminho do som

def clicker(): # funcao que vai ser usada para fazer o clicker
    playsom = playsom(som) # tocando o som
    while True: # loop infinito
        if clicking: # se o clicker estiver ativo
            mouse.click(Button.left, 1) # clique com o botão esquerdo do mouse
        time.sleep(0.2) # espere 0.2 segundos

def toggle_event(key): # função que vai ser usada para ativar e desativar o clicker
    if key == tecla:    # se a tecla apertada for a tecla que vai ser usada para ativar o clicker
        global clicking  # variável que vai ser usada para saber se o clicker esta ativo ou nao
        clicking = not clicking # inverte o valor da variável

click_thread = threading.Thread(target=clicker) # criando a thread que vai ser usada para fazer o clicker
click_thread.start() # iniciando a thread

with Listener(on_press=toggle_event) as listener: # criando o listener que vai ser usado para ativar e desativar o clicker
    listener.join() 
    
    

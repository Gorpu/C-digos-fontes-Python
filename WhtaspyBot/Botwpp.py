#Tenha as bibliotecas abaixo instaladas
#2-Crie um grupo com o nome bot_setting ou ajuste de acordo com a linha 39

from time import time
import keyboard as kb
import pyautogui as ptg
import time

while True:
    print('Automaçao Whats,py')
    menu=input('''Iniciar chat Bot 

[ENTER]''')
    if menu !='!':
        print("Iniciando...(15%)")
        time.sleep(3)
        #Abrir pela area de trabalho:
        kb.press_and_release('ctrl + d')
        print("Abrindo navegador...(20%)")
        time.sleep(0.8)
        print("Abrindo navegador...(25%)")
        kb.press_and_release('win')
        time.sleep(0.8)
        #inicializar
        kb.write("chrome")
        print("Abrindo navegador...(50%)")
        time.sleep(2)
        kb.press_and_release('enter')
        time.sleep(0.8)
        kb.write("web")
        print("Abrindo Web Whatsapp..(75%)")
        try:
            print("Sincronizando Conta...(80%)")
            time.sleep(0.8)
            kb.press_and_release("enter")
            time.sleep(20)
            ptg.click('win.PNG')
            print('Atualizando...(95%)')
            kb.write("bot_settings")
            time.sleep(2)
            print("Tudo Certo!!! (100%)")
            kb.press_and_release("enter")
            kb.write("""Bot em execuçao...
    Volte ao terminal""")
            kb.press_and_release("enter")
        except:
            input('Ocorreu um erro, whataspp não sicronizado no computador...[ENTER]')
        while True:
            menu_interno=input('''Enviar Lista de Transmição [1]
Progrmação Automatica [2]-Em desenvovimento''')
import sys
import wmi, platform, time
import PySimpleGUI as sg
import os
import keyboard as kb
import socket


#DEPENDENCIAS_1
c = wmi.WMI()
factory=c.Win32_ComputerSystem()[0]
#DEPENDENCIAS_2
plataforma = platform.uname()
#rede
ip=socket.gethostbyname(socket.gethostname())

def Janela_Menu():
    sg.theme('Topanga')
    layout=[
        [sg.Text("--------------------------------------------------")],
        [sg.Text("SISTEMA:")],
        [sg.Text(f"Fabricante: {factory.manufacturer}")],
        [sg.Text(f"Modelo: {factory.Model}")],
        [sg.Text(f"Arquitetura: {factory.SystemType} API: {sys.platform}")],
        [sg.Text("--------------------------------------------------")],
        [sg.Text(f"Sobre o Processador:")],
        [sg.Text(f"Processador: {plataforma.processor}")],
        [sg.Text(f"Cores: {os.cpu_count()}")],
        [sg.Button("Limpeza de Cache"),sg.Button("Sobre")],
        [sg.Text(" ------------------------------------------------")],
        [sg.Image(r"bg.png")]
        ]
    
    return sg.Window("Magicrow Clean", icon="icon.ico" , layout=layout,resizable=False, finalize=True, size=(620,480), font=('Consolas'))
    
janela1=Janela_Menu()
while True:
    window, event, values= sg.read_all_windows()
    if window == janela1 and event == "Limpeza de Cache":
        time.sleep(2)
        kb.press_and_release("win + r")
        time.sleep(0.8)
        kb.write("%temp%")
        time.sleep(0.8)
        kb.press_and_release("enter")
        time.sleep(6)
        kb.press_and_release("ctrl + a")
        kb.press_and_release("delete")
        time.sleep(120)
        kb.press_and_release("alt + f4")
    if window == janela1 and event == "Sobre":
        sg.popup_no_buttons('Magicrow Clean:\nVersão: 0.2b\nUpadate: 28-08-2022 UTC-3 16:46    ')
    if window == janela1 and event == sg.WIN_CLOSED:
        break
        
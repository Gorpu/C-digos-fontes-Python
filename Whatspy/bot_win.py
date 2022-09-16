import PySimpleGUI as sg
from random import randint
import keyboard as kb
import pyautogui as ptg
import time


n=0
m=1
void=" "*100000
erro_msng1='Desculpa, não consegui enteder!'
erro_msng2="Opss, desculpa mas eu não consegui entender."
erro_msng3="Peço desculpas mas, não consegui entender você."
error_ms02=[erro_msng1, erro_msng2, erro_msng3]

falar_vend="Que tal falar com nossos vendedores? Eles sempre estão prontos para melhor atender você."
falar_vend2="""Quer ficar por dentro de todas as promoções que acontecem aqui na Preço Baixo? 
Então salve o meu número para que você não perca nada que a gente postar nos status,
chame nossos vendedores no privado e aproveite!!!"""
falar_vend3="Olha agora que você já esta por dentro, vem correndo pra Preço Baixo da 402 sul! Ou entre em contato com os nossos vendedores para realizar a entrega."
falar_ven01=[falar_vend, falar_vend3, falar_vend2]

anexo_1="Aguarde irei enviar nossas promoções."
anexo_2="Com toda certeza você irá adorar nossas promoções, só um instantinho."
anexo_3='Gosta de ficar por dentro heim? Aguarde já estou mandando nossa mega promoção.'
anexo_frases=[anexo_1, anexo_2, anexo_3]

    
Promo="promo.png"
opr3="op3.png"
Venderores="contato.png"
imagenSttgsGroup="gp_setting.png"
anexo="ANEXO.png"
search_pdf_oferta="PESQUISA_OFERTA.png"
arquivo_wpp="arquivo_png.png"
pdf_promo="arquivobot.png"
send="enviar.png"
tres_p="tres_p.png"
apagar_msng="APAGAR_MSNG.png"
apagar_msng01="APAGAR_MSNG2.png"
apagar_msng2="APAGAR_MSNG_2.png"
icon_contatos="contatos.png"

#f###########  Funçoes    #############################

# "Reiniciar bot em caso de erro"
def erro_inesperado():
    time.sleep(3)
    grupo_bot()

# 'Apagar mensagem antes ou depois de responder algo para que não ocorra erros
def limpar_conversa():
    ptg.click(tres_p)
    time.sleep(2)
    ptg.click(1111, 348)
    time.sleep(3)
    ptg.click(777, 434)

# 'Grupo de Analise de Fucionamento do Bot"
def grupo_bot():
    try:
        ptg.click(imagenSttgsGroup)
        kb.write('''Rodando
        Precinho Bot''')
        kb.press_and_release("enter")
        time.sleep(2)
        try:
            time.sleep(2)
            ptg.click("janela.png")
            resposta_bot()
        except:
            time.sleep(5)
            resposta_bot()
    except:
        erro_inesperado()
        
# 'Responder outros clientes'  
def restart():
    resposta_bot()        

# "Interaçôes do Bot"   
def resposta_bot():
    
    while True:
        #funções Promoçoes e Vendedores
        def promoçoes_func():
            time.sleep(2)
            kb.write(anexo_frases_wpp)
            kb.press_and_release("enter")
            time.sleep(3)
            ptg.click(anexo)
            time.sleep(5)
            ptg.click(arquivo_wpp)
            time.sleep(3)
            ptg.click(pdf_promo)
            ptg.click(pdf_promo)
            time.sleep(3)
            ptg.click(send)
            time.sleep(10)
            ptg.click(Promo)
            time.sleep(2)
            ptg.click(tres_p)
            time.sleep(3)
            ptg.press("up")
            time.sleep(2)
            kb.press_and_release("enter")
            time.sleep(3)
            ptg.click(apagar_msng2)
            time.sleep(5)
            restart()
        def vendedores_func():
            time.sleep(2)
            kb.write("Aguarde alguns segundinhos, irei enviar os contatos de nossos vendedores.")
            kb.press_and_release("enter")
            #clicar no icone anexo
            ptg.click(anexo)
            time.sleep(5)
            #Clicar no icone enviar contatos
            ptg.click(icon_contatos)
            time.sleep(2)
            #pesquisar contatos
            kb.write("Bruno")
            time.sleep(2)
            kb.press_and_release("enter")
            kb.press_and_release("backspace")
            kb.write("Ana FPB 402 sul")
            time.sleep(2)
            kb.press_and_release("enter")
            kb.press_and_release("backspace")
            kb.write("Fábio FPB 402 sul")
            time.sleep(2)
            kb.press_and_release("enter")
            kb.press_and_release("backspace")  
            kb.write("Edvania FPB 402 sul")
            time.sleep(2)
            kb.press_and_release("enter")
            kb.press_and_release("backspace")      
            kb.write("Victor FPB 402 sul")
            time.sleep(2)
            kb.press_and_release("enter")
            kb.press_and_release("backspace")            
            #enviar contato
            ptg.click(send)
            time.sleep(2)
            ptg.click(send)
            time.sleep(3)
            ptg.moveTo(Venderores, duration=1)
            print("clicou no numero 2")
            time.sleep(4)
            ptg.click(tres_p)
            time.sleep(3)
            ptg.press("up")
            time.sleep(2)
            kb.press_and_release("enter")
            time.sleep(2)
            ptg.click(apagar_msng2)
            time.sleep(5)
            restart()
            
        #Inicio do loop após funções
        anexo_frases_rd=randint(0,2)
        anexo_frases_wpp=(anexo_frases[anexo_frases_rd])
        time.sleep(3)
        ptg.click(32,274)
        time.sleep(3)
        #locais
        ask=ptg.locateOnScreen(Promo)
        ask2=ptg.locateOnScreen(Venderores)
        if ask:
            promoçoes_func()
        if ask2:
            vendedores_func()
        if ask or ask2 ==None:
            #randomização_mensagem de erro pro cliente
            error_ms02_rd=randint(0,2) 
            error_ms02_wpp=(error_ms02[error_ms02_rd])
            falar_ven01_rd=randint(0,2)
            falar_ven01_wpp=(falar_ven01[falar_ven01_rd])
            ptg.moveTo(534, 594)
            #responder o cliente casoc ele não tenha digitado nem "1" ou "2"
            try:
                time.sleep(4)
                ptg.click(tres_p)
                time.sleep(3)
                ptg.press("up")
                time.sleep(2)
                kb.press_and_release("enter")
                time.sleep(3)
                ptg.click(apagar_msng2)
                time.sleep(5)
                #enviar opções
                kb.write(error_ms02_wpp)
                time.sleep(3)
                kb.press_and_release("enter")
                time.sleep(3)
                kb.write(falar_ven01_wpp)
                time.sleep(2)
                kb.press_and_release("enter")
                time.sleep(3)
                kb.write("/olá1")
                time.sleep(1)
                kb.press_and_release("enter")
                time.sleep(2)
                kb.press_and_release("enter")
                limpar_conversa()
                time.sleep(5)
                ptg.click(32, 275)
                restart()
            except:
                restart()
 # "Iniciar Bot"        
def bot_init():
    #variavel reconhecida em outro script
    kb.press_and_release("win + r")
    time.sleep(2)
    kb.write('chrome')
    kb.press_and_release('enter')
    time.sleep(3)
    kb.write('web.whatsapp.com')
    kb.press_and_release("enter")
    try:
        
        time.sleep(0.5)
        grupo_bot()
    except:
        erro_inesperado()
###############" Janelas"##############
def menuprincipal():
    layout=[
        [sg.Button("Iniciar")]
    ]
    return sg.Window("Bender Bot", layout=layout, grab_anywhere=True, finalize=True, size=(400,400))
janela1=menuprincipal()
janela2=None
while True:
    window, event, values=sg.read_all_windows()
    if window == janela1 and event == "Iniciar":
        print("time")
        time.sleep(2)
    if window == janela1 and event == sg.WIN_CLOSED:
        break
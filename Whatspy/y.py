from random import randint
from tokenize import group
import keyboard as kb
import pyautogui as ptg
import time
from colorama import init, Fore, Back, Style
from sty import fg, bg, ef, rs 

void=" "*100000
erro_msng1='Olá tudo bem?Atendente virtual Precinho aqui. É uma honra poder atender você, aguarde um pouquinho, não demoro.'
erro_msng2="Iai como você está? Me chamo Precinho seu atendente virtual e irei ajudar no seu atendimento. Fico grato por ter entrado em contato com a Preço Baixo da 402 sul; Espere só mais um pouquinho, serei breve.."
erro_msng3="Tudo bão com você uai? Sou o seu atendente virtual, me chamo Precinho irei lhe ajudar a ser atendido com mais agilidade, desde já fico super feliz e agradecido pelo seu contato, aguarde um intantinho..."
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
click_msng="click_msng.png"
filtro_conv="filtro_conversas.png"
limpar_mensagens='limparar_msgn.png'
limpar_mensagens_2='limparar_msgn2.png'
#f###########  Funçoes    #############################

# "Reiniciar bot em caso de erro"
def erro_inesperado():
    time.sleep(3)
    grupo_bot()

def erro_inesperado2():
    time.sleep(3)
    resposta_bot()
    
# 'Apagar mensagem antes ou depois de responder algo para que não ocorra erros
def limpar_conversa():
    time.sleep(3)
    ptg.click(1241, 93)
    time.sleep(3)
    ptg.click(1130, 352)
    time.sleep(3)
    ptg.click(740, 430)

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
        erro_inesperado2()
        
# 'Responder outros clientes'  
def restart():
    resposta_bot()        


# "Interaçôes do Bot"   
def resposta_bot():
    while True:
        anexo_frases_rd=randint(0,2)
        anexo_frases_wpp=(anexo_frases[anexo_frases_rd])
        
        
        def notAsk1_Ask2():
            error_ms02_rd=randint(0,2) 
            error_ms02_wpp=(error_ms02[error_ms02_rd])
            falar_ven01_rd=randint(0,2)
            falar_ven01_wpp=(falar_ven01[falar_ven01_rd])
            time.sleep(1)
            ptg.click(tres_p)
            time.sleep(0.5)
            ptg.press("up")
            time.sleep(0.5)
            kb.press_and_release("enter")
            time.sleep(2)
            ptg.click(apagar_msng2)
            time.sleep(0.5)
            #enviar opções
            kb.write(error_ms02_wpp)
            time.sleep(0.3)
            kb.press_and_release("enter")
            time.sleep(1)
            kb.write(falar_ven01_wpp)
            time.sleep(1)
            kb.press_and_release("enter")
            time.sleep(1)
            kb.write("/olá1")
            time.sleep(1)
            kb.press_and_release("enter")
            time.sleep(1)
            kb.press_and_release('enter')
            time.sleep(0.5)
            ptg.click(imagenSttgsGroup)
            time.sleep(2)
            resposta_bot()
    
                
            

            
        #funções Promoçoes e Vendedores
        def promoçoes_func():
            time.sleep(2)
            limpar_conversa()
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
            time.sleep(2)
            #enviar menu
            kb.write("/olá1")
            time.sleep(2)
            kb.press_and_release("enter")
            time.sleep(0.6)
            kb.press_and_release('enter')
            time.sleep(0.3)
            #voltar a espera de mensagens
            ptg.click(imagenSttgsGroup)
            resposta_bot()
            
        def vendedores_func():
            limpar_conversa()
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
            time.sleep(1.5)
            kb.press_and_release("enter")
            kb.press_and_release("backspace")
            kb.write("Ana FPB 402 sul")
            time.sleep(1.5)
            kb.press_and_release("enter")
            kb.press_and_release("backspace")
            kb.write("Fábio FPB 402 sul")
            time.sleep(1.5)
            kb.press_and_release("enter")
            kb.press_and_release("backspace")  
            kb.write("Edvania FPB 402 sul")
            time.sleep(1.5)
            kb.press_and_release("enter")
            kb.press_and_release("backspace")      
            kb.write("Victor FPB 402 sul")
            time.sleep(1.5)
            kb.press_and_release("enter")
            kb.press_and_release("backspace")            
            #enviar contato
            ptg.click(send)
            time.sleep(2)
            ptg.click(send)
            time.sleep(3)
            #enviar menu
            kb.write("/olá1")
            time.sleep(2)
            kb.press_and_release("enter")
            time.sleep(0.6)
            kb.press_and_release("enter")
            #apagar mensagem
            time.sleep(0.5)
            ptg.click(imagenSttgsGroup)
            resposta_bot()
            
                        
        #Inicio do loop após funções
        try:
            time.sleep(1)
            ptg.moveTo(click_msng, duration=0.6)
            time.sleep(2)
            ptg.click(click_msng)
            time.sleep(2)
            #locais
            ask=ptg.locateOnScreen(Promo)
            ask2=ptg.locateOnScreen(Venderores)
            if ask:
                ptg.moveTo(534, 594)
                promoçoes_func()
            if ask2:
                ptg.moveTo(534, 594)
                vendedores_func()
            if ask or ask2 ==None:
                #randomização_mensagem de erro pro cliente
                ptg.moveTo(534, 594)
                #responder o cliente casoc ele não tenha digitado nem "1" ou "2"
                try:
                    notAsk1_Ask2()
                except:
                    resposta_bot()
                    
        except:
            erro_inesperado2()
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
        
while True:
    init(autoreset=True)
    mainMenu=input("""
============================
 Bender Bot:                             
============================

>>Iniciar [Enter]                               
                                                       
----------------------------------------------
Desenvolvedor: L R Ferreira (Gorpo)
Github: https://github.com/Gorpu
-----------------------------------------------""")
    if mainMenu != 'ASD':
        print("\n")
        bot_init()
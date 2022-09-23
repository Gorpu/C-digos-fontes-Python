from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import keyboard as kb
import os
import time

promoção_pdf=os.path.abspath('C:/Users/Maranhao/Desktop/BOT/oferta.pdf')

frase_bot='Bot diz Oi'

def listen():
    while True:
        time.sleep(1)

service = Service(ChromeDriverManager(). install())
navegador = webdriver.Chrome(service=service)
navegador.get('https://web.whatsapp.com/')
time.sleep(40)

def enviar_promo():
    navegador.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/div/span').click()
    navegador.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/span/div/div/ul/li[4]/button/input').send_keys(promoção_pdf)
    time.sleep(5)
    navegador.find_element(By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/div/div[2]/div[2]/div/div/span').click()

    
def enviar_msng():
    navegador.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p').send_keys(frase_bot)
    time.sleep(3)
    navegador.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button/span').click()
    enviar_promo()
    #navegador.find_element(By.CSS_SELECTOR, '[title="Diplobot"]').click()
    
    
def bot_init():
    uma_msng = '[aria-label="1 mensagem não lida"]'
    duas_msng = '[aria-label="2 mensagens não lidas"]'
    while True:
        try:
            navegador.find_element(By.CSS_SELECTOR, f'{uma_msng}').click()
            enviar_msng()
        except:
            try:
                navegador.find_element(By.CSS_SELECTOR, f'{duas_msng}').click()
                enviar_msng()
            except:   
                print('Sem Mensagens!!!')
                time.sleep(5)
                bot_init()
bot_init()

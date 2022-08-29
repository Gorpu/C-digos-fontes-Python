from inspect import _void
from multiprocessing import Event
import matplotlib.pyplot as plt
import time
import pygame

pygame.init()
tempo=time.localtime()

dia=tempo[2]
mes=tempo[1]
ano=tempo[0]

ns=0
ac=0
quantidade = 0

leites=[]
quan=[]

void = ' '*10000
input("""
Analise de Rentabilidade mensal e Média Diaria
          
Versão: 0.1
Autor: Liedson Rocha
Aperte [ENTER] para coninuar""")
while True:
    print(f'''{void}''')
    ac+=1
    print(f"Dia {ac}")
    quantidade1=int(input("Valor Diário Obtido: "))
    quantidade=quantidade1
    ns+=quantidade
    ad=input("Continuar?(s/n) ")
    if ad=="s":
        leites.append(f"dia {ac}")
        quan.append(quantidade)
    if ad=="n":
        leites.append(f"dia {ac}")
        quan.append(quantidade)
#Espaço entre as barras
        fig, ax = plt.subplots(figsize=(8, 5))
#Grafico
        ax.bar(leites, quan, color=["red", "green", "brown"])
        for idx, val in enumerate(quan):
            txt = f"{val} R$"
            y_l= val
            x_l = idx
            nt = ns/ac
            ax.text(y=y_l, x=x_l, s=txt, fontsize=10)
            plt.title(f"Vendas {mes}/{ano}")
            plt.ylabel("Total em R$:")
            plt.xlabel(f"""Valor Somado: R${ns} 
    Média Diária: R${nt}""")
            ax.grid()
            plt.show()
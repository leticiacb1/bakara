# EP - Design de Software
# Equipe: Letícia Coêlho Barbosa
# Data: 17/10/2020

import random as r
import math
from os import system, name 
import time

def clear():         
   
    if name == 'nt': 
        _ = system('cls') 
  
    else: 
        _ = system('clear') 

def puxa_carta(lista):   #função que recebe uma lista, sortea um valor e adiciona na lista
    global baralho

    carta=r.choice(baralho)

    lista.append(carta)
    baralho.remove(carta)

    return lista


def soma_cartas(lista):      # Função que recebe uma lista e soma seus itens
    global dicionario_cartas
    soma=0

    for i in range(len(lista)):
        soma+=dicionario_cartas[lista[i]]

    soma = soma%10   #garante que a soma não ultrapasse 9

    return soma

#Definindo um dicionario de cartas
dicionario_cartas = {
    'A':1,
    '2':2,
    '3':3,
    '4':4,
    '5':5,
    '6':6,
    '7':7,
    '8':8,
    '9':9,
    '10':0,
    'J':0,
    'Q':0,
    'K':0
}

clear()

print("*********************************************")
print("********** BEM VINDO AO BACARÁ !!! **********")
print("*********************************************")

print("\n")

#Adicioando mais baralhos
qtde_baralhos=int(input("Com quantos baralhos quer jogar? (1 , 6 ou 8)\n>>>> "))
baralho = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']*4*qtde_baralhos   

num_jogadores=int(input("Quantos jogadores irão jogar?\n>>>> "))    #Implementação Mais jogadores

qtde_jogador=10000  #Estipulando valor de inicio 

lista_qtde_jogadores=[qtde_jogador for i in range(num_jogadores)]   #Uma lista com os valores inicias de cada jogador
lista_jogador_continua = [True for i in range(num_jogadores)]       #Uma lista para jogadores que permanecem na partida

while(True in lista_jogador_continua):   #Loop será realizado sempre que houver pelo menos 1 jogador querendo continuar
    clear()

    mao_jogador = []           #Listas serão inicializadas a cada loop
    mao_banco = []
    lista_aposta_jogadores=[]  #Guardará as apostas de cada jogador

    #Distribuindo as cartas
    
    mao_jogador=puxa_carta(mao_jogador)    
    mao_jogador=puxa_carta(mao_jogador)
    
    mao_banco=puxa_carta(mao_banco)
    mao_banco=puxa_carta(mao_banco)

    #Somando cartas

    soma_jogador = soma_cartas(mao_jogador)
    soma_banco = soma_cartas(mao_banco)

    #Condições para a terceira carta jogador:
    if(soma_banco<8):
        
        if(soma_jogador<=5):  
            mao_jogador=puxa_carta(mao_jogador) 
            soma_jogador=soma_cartas(mao_jogador)
            ultima_jogador=dicionario_cartas[mao_jogador[2]]
            
    #Condições para terceira cartas banco:

    if(soma_jogador<8):
        if(len(mao_jogador)<3):
            if(soma_banco<=5):
                mao_banco=puxa_carta(mao_banco)
                soma_banco=soma_cartas(mao_banco)
        else:
            if(soma_banco<=5):
                if(soma_banco==3):
                    if(ultima_jogador != 8):
                        mao_banco=puxa_carta(mao_banco)
                        soma_banco=soma_cartas(mao_banco)
                        
                elif(soma_banco==4):
                    if(ultima_jogador not in [0,1,8,9]):
                        mao_banco=puxa_carta(mao_banco)
                        soma_banco=soma_cartas(mao_banco)

                elif(soma_banco==5):
                    if(ultima_jogador not in [0,1,2,3,8,9]):
                        mao_banco=puxa_carta(mao_banco)
                        soma_banco=soma_cartas(mao_banco)
                
                else:
                    mao_banco=puxa_carta(mao_banco)
                    soma_banco=soma_cartas(mao_banco)

    #Descobrindo o vencedor

    if(soma_jogador==soma_banco):
        resultado='empate'
    if(soma_jogador>soma_banco):
        resultado='jogador'    
    if(soma_banco>soma_jogador):
        resultado='banco'
    
    for i in range(num_jogadores):      #Loop ocorrerá para cada jogador
        if(lista_jogador_continua[i]):  #Certificando que apenas jogadores que estão na partida irão jogar
            clear()
        
            print("Turno Jogador ",i+1)
            print("Você possui {} moedas".format(lista_qtde_jogadores[i]))
            valor=int(input("Quanto você quer apostar?\n>>>> "))

            while(valor>lista_qtde_jogadores[i]):
                print("DIGITE UM VALOR VÁLIDO!\n")
                valor=int(input("Quanto você quer apostar?\n>>>> "))
                
            aposta=input("Aposte em jogador, banco ou empate:\n>>>> ")
            lista_aposta_jogadores.append(aposta)   #Adicionando apostas de cada jogador

            #Pagando a aposta

            if(aposta==resultado):   #VITÓRIA
                
                if(resultado=='empate'):

                    ganho=8*valor

                    #Adicionando comissão da casa:
                    if(qtde_baralhos==1):
                        comissao=0.1575*ganho
                    elif(qtde_baralhos==6):
                        comissao=0.1444*ganho
                    elif(qtde_baralhos==8):
                        comissao=0.1436*ganho  

                    #Recalculando ganho:
                    ganho=math.floor(ganho-comissao)
                
                if(resultado=='jogador'):
                    
                    ganho=valor

                    #Adicionando comissão da casa:
                    if(qtde_baralhos==1):
                        comissao=0.0129*ganho
                    elif(qtde_baralhos==6):
                        comissao=0.0124*ganho
                    elif(qtde_baralhos==8):
                        comissao=0.0124*ganho

                    #Recalculando ganho:
                    ganho=math.floor(ganho-comissao)
                
                if(resultado== 'banco'):
                    
                    ganho=math.floor(0.95*valor)

                    #Adicionando comissão da casa:
                    if(qtde_baralhos==1):
                        comissao=0.0101*ganho
                    elif(qtde_baralhos==6):
                        comissao=0.0106*ganho
                    elif(qtde_baralhos==8):
                        comissao=0.0106*ganho
                    
                    #Recalculando ganho:
                    ganho=math.floor(ganho - comissao)
                
                lista_qtde_jogadores[i]+=ganho   #Adicionando ganho do jogador i na lista de valores
                

            else:   ##PERDEU
                lista_qtde_jogadores[i]-=valor   #Retirando valor apostado

    clear()

    #Agora o resultado do jogo será exibido na tela:

    print("********** Começando o jogo **********\n")

    print("Cartas do jogador são: {} e {}".format(mao_jogador[0],mao_jogador[1]))
    print("As cartas do banco são: {} e {}".format(mao_banco[0],mao_banco[1]))

    if(len(mao_jogador)==3):
        print("\n")
        print("Jogador pega a terceira carta")
        print("As cartasdo jogador são: {0},{1} e {2}".format(mao_jogador[0],mao_jogador[1],mao_jogador[2]))   

    if(len(mao_banco)==3):
        print("\n")
        print("Banco pegou a terceira carta")

    print("\n")    
    print("Soma do jogador é {}".format(soma_jogador))
    print("Soma banco é {}".format(soma_banco))

    print("O resultado da partida foi : {}".format(resultado))

    time.sleep(5)
    clear()

    j=0                                   #Index para a lista_aposta_jogadores 
    for i in range(num_jogadores):        #Realizando a ação de Jogador por Jogador
        if(lista_jogador_continua[i]):                  #Para os jogadores que estão na partida (True)
            if(lista_aposta_jogadores[j]==resultado):
                print("\n")
                print("Jogador {} ganhou!".format(i+1))
                print("Agora você possui {} moedas".format(lista_qtde_jogadores[i]))
            else:
                print("\n")
                print("Jogador {} perdeu!".format(i+1))
                print("Agora você possui {} moedas".format(lista_qtde_jogadores[i]))

                if(lista_qtde_jogadores[i]==0):              #Jogador que perdeu tudo
                    print("Você perdeu tudo!")
                    print("FIM DE JOGO PRA VOCÊ, MEU CHAPA!") 
                    lista_jogador_continua[i] = False        #Retirando o jogador que perdeu tudo da partida
            
            j+=1
            time.sleep(2)
            
        if(lista_jogador_continua[i]):                       #Para jogadores que estão na partida (True)
            clear()
            continua=input("Jogador {} gostaria de continuar o jogo? (S/N)\n>>>> ".format(i+1))
            
            if(continua == 'S'):                             #Mudando lista para aqueles que querem ou não continuar o jogo
                lista_jogador_continua[i] = True
                clear()
            if(continua== 'N'):
                lista_jogador_continua[i] = False
                clear()
                print("Obrigada por jogar!")

print("FIM DE JOGO!")

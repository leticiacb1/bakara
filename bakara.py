
# EP - Design de Software
# Equipe: Letícia Coêlho Barbosa
# Data: 15/10/2020

import random as r
import math
from os import system, name 

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

qtde_jogador=10000
print("Você possui {} moedas".format(qtde_jogador))

valor=int(input("Quanto quer apostar?\n>>>> "))

resposta=True #variável controle do loop

while resposta:
    clear()
    if(valor<=qtde_jogador):
        mao_jogador = []     #Listas serão inicializadas a cada loop
        mao_banco = []
       
        aposta=input("Aposte em jogador, banco ou empate:\n>>>> ")
        clear()

        #Distribuindo as cartas
        
        mao_jogador=puxa_carta(mao_jogador)    
        mao_jogador=puxa_carta(mao_jogador)
        
        mao_banco=puxa_carta(mao_banco)
        mao_banco=puxa_carta(mao_banco)

        print("Suas cartas são: {} e {}".format(mao_jogador[0],mao_jogador[1]))
        print("As cartas do banco são: {} e {}".format(mao_banco[0],mao_banco[1]))

        #Somando cartas

        soma_jogador = soma_cartas(mao_jogador)
        soma_banco = soma_cartas(mao_banco)

        print("Sua soma é {}".format(soma_jogador))
        print("Soma banco é {}".format(soma_banco))

        #Condições para a terceira carta jogador:
        if(soma_banco<8):
            
            if(soma_jogador<=5):  
                mao_jogador=puxa_carta(mao_jogador) 
                soma_jogador=soma_cartas(mao_jogador)
                ultima_jogador=dicionario_cartas[mao_jogador[2]]
                
                print("\n")
                print("Pegando a terceira carta")
                print("Suas cartas são: {0},{1} e {2}".format(mao_jogador[0],mao_jogador[1],mao_jogador[2]))   
                print("Sua soma agora é {}".format(soma_jogador))

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
                            
                            print("\n")
                            print("Banco pegou a terceira carta")
                            print("Soma banco: {}".format(soma_banco))

                    elif(soma_banco==4):
                        if(ultima_jogador not in [0,1,8,9]):
                            mao_banco=puxa_carta(mao_banco)
                            soma_banco=soma_cartas(mao_banco)

                            print("\n")
                            print("Banco pegou a terceira carta")
                            print("Soma banco: {}".format(soma_banco))

                    elif(soma_banco==5):
                        if(ultima_jogador not in [0,1,2,3,8,9]):
                            mao_banco=puxa_carta(mao_banco)
                            soma_banco=soma_cartas(mao_banco)

                            print("\n")
                            print("Banco pegou a terceira carta")
                            print("Soma banco: {}".format(soma_banco))
                    
                    else:
                        mao_banco=puxa_carta(mao_banco)
                        soma_banco=soma_cartas(mao_banco)

                        print("\n")
                        print("Banco pegou a terceira carta")
                        print("Soma banco: {}".format(soma_banco))

        #Descobrindo o vencedor

        if(soma_jogador==soma_banco):
            resultado='empate'
        if(soma_jogador>soma_banco):
            resultado='jogador'    
        if(soma_banco>soma_jogador):
            resultado='banco'

        print('\n')
        print("Você havia aposta em : {}". format(aposta))
        print("O resultado foi : {}".format(resultado))

        #Pagando a aposta

        if(aposta==resultado):   #Vitória
            
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
                ganho=math.ceil(ganho-comissao)
            
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
                ganho=math.ceil(ganho-comissao)
            
            if(resultado== 'banco'):
                
                ganho=math.ceil(0.95*valor)

                #Adicionando comissão da casa:
                if(qtde_baralhos==1):
                    comissao=0.0101*ganho
                elif(qtde_baralhos==6):
                    comissao=0.0106*ganho
                elif(qtde_baralhos==8):
                    comissao=0.0106*ganho
                
                #Recalculando ganho:
                ganho=math.ceil(ganho - comissao)
            
            qtde_jogador+=ganho
            
            print("\n")
            print("Você ganhou {} modedas!".format(ganho))
            print("Agora você possui {} moedas". format(qtde_jogador))

        else:
            print("\n")
            print("Você perdeu {} modedas!".format(valor))
            qtde_jogador-=valor
            print("Agora você possui {} moedas". format(qtde_jogador))
            
        #Mudando a variável que mantém o loop
        
        if(qtde_jogador != 0):
            print("\n")    
            continua=input("Gostaria de continuar o jogo? (S/N)\n>>>> ")
            
            if(continua == 'S'):
                resposta= True
                clear()
                print("Você possui {} moedas". format(qtde_jogador))
                valor=int(input("Quanto quer apostar?\n>>>> "))
            else:
                resposta= False
                clear()
                print("Obrigada por jogar!")
        else:
            print("Você perdeu tudo!")
            resposta=False 
    else:
        print("Você não possui fichas o suficiente")
        print("Você possui {} moedas". format(qtde_jogador))
        valor=int(input("Quanto quer apostar?\n>>>> "))
    
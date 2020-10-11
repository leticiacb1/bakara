
import random as r
import math


def puxa_carta(lista):
    global baralho

    carta=r.choice(baralho)

    lista.append(carta)
    baralho.remove(carta)

    return lista


def soma_cartas(lista):
    global dicionario_cartas
    soma=0

    for i in range(len(lista)):
        soma+=dicionario_cartas[lista[i]]

    soma = soma%10

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

#Adicioando mais baralhos
qtde_baralhos=int(input("Quantos baralhos? "))
baralho = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']*4*qtde_baralhos

qtde_jogador=100
valor=int(input("Quanto quer apostar?"))

mao_jogador = []
mao_banco = []

resposta=True #variável controle do loop

while resposta:
    if(valor<qtde_jogador):
        
        aposta=input("Aposte em jogador, banco ou empate ")

        #Distribuindo as cartas
        
        mao_jogador=puxa_carta(mao_jogador)
        mao_jogador=puxa_carta(mao_jogador)
        
        mao_banco=puxa_carta(mao_banco)
        mao_banco=puxa_carta(mao_banco)

        #Somando cartas

        soma_jogador = soma_cartas(mao_jogador)
        soma_banco = soma_cartas(mao_banco)
        
        if(soma_banco<8):
            if(soma_jogador<=5):  #Condição para 3 carta 
                mao_jogador=puxa_carta(mao_jogador) 
                soma_jogador=soma_cartas(mao_jogador)
                ultima_jogador=dicionario_cartas[mao_jogador[2]]
                    


    else:
        print("Você não possui fichas o suficiente")
    
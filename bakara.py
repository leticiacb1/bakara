
import random as r

n=100  #Numero de fichas iniciais do jogador

print("Você possui {0} fichas".format(n))

jogador=[] #Cartas recebidas pelo jogador
banco=[] #Cartas recebidas pelo banco

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


baralho = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']*4


while resposta:

    valor=int(input("Quanto quer apostar? "))

    if(valor<=n):

        aposta=input("Em quem deseja apostar? (jogador/banco ou empate) ")

        
        # Distribuindo 2 cartas para o jogador e para o banco   
        for i in range(2):
            
            #Sorteando cartas do jogador:
            
            j=r.choice(baralho)
            jogador.append(j)    
            baralho.remove(j)    #Retirar a carta do baralho

            #Sorteando cartas para o banco:

            b=r.choice(baralho)
            banco.append(b)    
            baralho.remove(b)    #Retira a carta do baralho

        print("Suas cartas: {0} e {1}".format(jogador[0],jogador[1]))
        print("Suas cartas: {0} e {1}".format(banco[0],banco[1]))

        #Calculando a soma
        soma1_jogador=jogador[0]+jogador[1]  #Primeira soma de cartas jogador
        soma1_banco=banco[0]+banco[1]        #Primeira soma de cartas banco

        print("Sua soma: {0}".format(soma1_jogador))

        #Descobrindo o vencedor
        if((soma1_jogador==8 or soma1_jogador%10==8) or (soma1_jogador==9 or soma1_jogador%10==9)):
            vencedor='jogador'

        elif((soma1_banco==8 or soma1_banco%10==8) or (soma1_banco==9 or soma1_banco%10==9)):
            vencedor='banco'
        
        elif((soma1_jogador==soma1_banco==8 or soma1_jogador%10==soma1_banco%10==8) or ((soma1_jogador==soma1_banco==9 or soma1_jogador%10==soma1_banco%10==9))):
            vencedor='empate'
        
        else: #Distribuindo uma terceira carta
            if((soma1_jogador==7 or soma1_jogador%10==7) or (soma1_jogador==6 or soma1_jogador%10==6)):
                #Não distribui a terceira carta pro jogador
            
            elif((soma1_banco==7 or soma1_banco%10==7) or (soma1_banco==6 or soma1_banco%10==6)):
                #Não distribui a terceira carta para o banco
            
            
        #Ganhador:
        if(vencedor=='jogador' and (aposta== 'jogador' or aposta== 'Jogador')):

        elif(vencedor=='banco' and (aposta=='banco' or aposta=='Banco')):

        elif (vencedor=='empate' and (aposta== 'empate' or aposta== 'empate')):    

        else:
            print("Valor inválido inserido")    


    else:
        print("Você não possui fichas o suficiente")

    resposta=input("Gostaria de continuar jogando (S/N)? ")

    while(resposta!='N' or resposta!='S')
        
        if(resposta=='N'):
            resposta= False
        elif(resposta=='S'):
            resposta True
        else:
            print("Valor incorreto")
            resposta=input("Gostaria de continuar jogando (S/N)? ")
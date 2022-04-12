from traceback import print_tb
from cv2 import bilateralFilter
from sqlalchemy import false
import random


def jogar():
    
    imprime_mensagem_abertura()

    palavra_secreta = abertura_de_arquivo()

    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)
    
    
    letras_erradas = []
    letras_chutadas = []
    separador = list(palavra_secreta)

    
    enforcou = False
    acertou = False
    totalDeTentativas = 10
    tentativas = 1
    erros = 0

    while(not enforcou and not acertou):

        chute = input("Qual a Letra ?")
        chute = chute.strip().upper()
        chute = chute[0]

        if (chute not in letras_chutadas):
            letras_chutadas.append(chute)
            if(tentativas < totalDeTentativas):
                if (chute in palavra_secreta):
                    index = 0
                    for letra in palavra_secreta:
                        if(chute == letra):
                            letras_acertadas[index] = letra
                        index = index + 1

                    print("Tentativa {} de {} ".format(tentativas, totalDeTentativas))
                    print("Você acertou")
                    print(letras_acertadas)
                    tentativas += 1
                    
                
                else:

                    letras_erradas.append(chute)
                    print("Tentativa {} de {} ".format(tentativas, totalDeTentativas))
                    print("A palavra secreta não possui essas letras ! {} ".format(letras_erradas))
                    tentativas += 1
                    erros += 1

            else:
                
                print("Você usou todas as suas tentativas")
                
                break
        
        else:
            print("Você já chutou essa letra !")
            print("Letras já chutadas {}".format(letras_chutadas))
        
        acertou = "_" not in letras_acertadas
    
    if(acertou):
        print("PARABÉNS VOCÊ GANHOU")
    else:
        print(f"Sinto muito você PERDEU, a palavra secreta era {palavra_secreta}")  


    print("Fim do jogo")




def imprime_mensagem_abertura():
   
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")


def abertura_de_arquivo():
    with open("palavras.txt", "r") as arquivo:
    
        palavras = []

        for linha in arquivo:
            linha = linha.strip()
            palavras.append(linha)

    numero = random.randrange(0,len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta



def inicializa_letras_acertadas(palavra):
        return ["_" for letra in palavra]
        


if(__name__ == "__main__"):
    jogar()

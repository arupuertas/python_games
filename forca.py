import random

def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")


    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0,len(palavras))
    palavra_secreta = palavras[numero]

    # palavra_secreta = "python"
    letras_acertadas = ["_"]
    letras_chutadas = []
    palavras_campo = len(palavra_secreta)
    print("A palavra tem {} letras".format(palavras_campo))


    while True:
    
        if len(palavra_secreta) > len(letras_acertadas):
            letras_acertadas.append("_")
        
        else:
            break

    enforcou = False
    acertou = False

    # Função .find() qual posição está uma letra que é passada

    # Funções .methods()

    # Enquanto (TRUE E TRUE)
    # print("Qual é a palavra ?")
    print(letras_acertadas)
    print()

    while(not enforcou and not acertou):

        chute = input("Qual letra? ")
        chute = chute.strip()
        letras_usadas = chute
        letras_chutadas.append(letras_usadas)

        index = 0
        for letra in palavra_secreta:
            if(chute.upper() == letra.upper()):
                letras_acertadas[index] = letra

                # print("Encontrei a letra {} na posição {}".format(letra, index))
            index = index + 1
            
        print("você chutou as letras {}".format(letras_chutadas))
        print(letras_acertadas)
        print()

    print("Fim do jogo")


if(__name__ == "__main__"):
    jogar()

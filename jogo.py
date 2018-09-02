import random

enforcou = False
acertou = False
erros = 0

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
palavra_chave = palavras[numero].upper()
letras_acertadas = ["_" for letra in palavra_chave]

while (not enforcou and not acertou):
    chute = input("Qual é a letra? ")
    chute = chute.strip().upper()

    if(chute in palavra_chave):
        index = 0
        for letra in palavra_chave:
            if(chute.upper() == letra.upper()):
                letras_acertadas[index] = letra
            index += 1
    else:
        erros +=1
        print(erros)

    enforcou = erros == 6
    acertou = "_" not in letras_acertadas
    print(letras_acertadas)

if(acertou):
    print("Parabens!! Você ganhou o jogo")
else:
    print("Desculpe... Você perdeu o jogo")

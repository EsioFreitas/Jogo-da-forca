palavra_chave = "banana"
enforcou = False
acertou = False
erros = 0
letras_acertadas = ["_" for letra in palavra_chave]

print("*********************************")
print("***Bem vindo ao jogo da Forca!***")
print("*********************************")

while (not enforcou and not acertou):
    chute = input("Qual é a letra? ")
    chute = chute.strip()

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

palavra_chave = "banana"

enforcou = False
acertou = False

while (not enforcou and not acertou):
    chute = input("Qual é a letra? ")
    chute = chute.strip()

    index = 0
    for letra in palavra_chave:
        if(chute.upper() == letra.upper()):
            print("Encontrei a letra {} na posição {}".format(letra, index))
        index += 1

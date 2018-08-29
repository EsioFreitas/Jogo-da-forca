palavra_chave = "banana"

enforcou = False
acertou = False
letras_acertadas = ["_","_","_","_","_","_",]

while (not enforcou and not acertou):
    chute = input("Qual é a letra? ")
    chute = chute.strip()

    index = 0
    for letra in palavra_chave:
        if(chute.upper() == letra.upper()):
            letras_acertadas[index] = letra
        index += 1

    print(letras_acertadas)

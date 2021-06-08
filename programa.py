import random

letras = "abcdefghijklmnopqrstuvwxyzçABCDEFGHIJKLMNOPQRSTUVWXYZÇ"
numeros = "0123456789"
simbulos = "!@#$%&*()_-=+"

while True:
    print("\nCrie sua senha de uma maneira totalmente aleatória e segura!!\n")

    # escolha de quais tipos de caracteres o usuario deseja usar
    perg_letras = input("Deseja usar letras? [s/n]: ")
    perg_nums = input("Deseja usar numeros? [s/n]: ")
    perg_simbs = input("Deseja usar símbulos? [s/n]: ")
    tamanho_senha = int(input("\nDigite o tamanho da senha (recomendado: 8 - 16): "))

    # tratamento de erro
    while tamanho_senha > 50 or tamanho_senha < 1:
        tamanho_senha = int(input("\nDigite o tamanho da senha (recomendado: 8 - 16): "))

    senha = ""
    while len(senha) != tamanho_senha:
        # decide aleatoriamente qual dos tres sera adicionado
        letra_num_ou_simb = random.randint(0, 2)

        if letra_num_ou_simb == 0 and perg_letras == "s":
            letra_aleatoria = (letras[random.randint(0, 53)])
            senha = senha + letra_aleatoria

        elif letra_num_ou_simb == 1 and perg_nums == "s":
            num_aleatorio = (numeros[random.randint(0, 9)])
            senha = senha + num_aleatorio

        elif letra_num_ou_simb == 2 and perg_simbs == 's':
            simb_aleatoria = (simbulos[random.randint(0, 12)])
            senha = senha + simb_aleatoria

    print(f"\nSenha: {senha}")

    denovo = input("\nDeseja usar o programa denovo? [s/n]: ")
    if denovo == 'n':
        break
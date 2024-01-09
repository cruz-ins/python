def str1241():
    print("BEE 1174 - Encaixa ou Não II")
    print("Paulinho tem em suas mãos um novo problema. Agora a sua professora lhe pediu que construísse um programa para verificar, à partir de dois valores muito grandes A e B, se B corresponde aos últimos dígitos de A.")
    print("Entrada")
    print("A entrada consiste de vários casos de teste. A primeira linha de entrada contém um inteiro N que indica a quantidade de casos de teste. Cada caso de teste consiste de dois valores A e B maiores que zero, cada um deles podendo ter até 1000 dígitos.")
    print("Saída")
    print("Para cada caso de entrada imprima uma mensagem indicando se o segundo valor encaixa no primeiro valor, confome exemplo abaixo.")
    while True:
        # Lê o número de casos de teste
        n = int(input())

        # Para cada caso de teste
        for _ in range(n):
            # Lê os números A e B como strings
            a, b = input().split()

            # Verifica se B corresponde aos últimos dígitos de A
            if a.endswith(b):
                print("encaixa")
            else:
                print("nao encaixa")
        if input("Continuar Loop: 1 para continuar, 2 para sair") == "2": break
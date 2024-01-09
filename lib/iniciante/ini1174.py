def ini1174():
    print("BEE 1174 - Seleçao em Vetor I")
    print("Faça um programa que leia um vetor A[100]. No final, mostre todas as posições do vetor que armazenam um valor menor ou igual a 10 e o valor armazenado em cada uma das posições.")
    print("Entrada")
    print("A entrada contém 100 valores, podendo ser inteiros, reais, positivos ou negativos.")
    print("Saída")
    print("Para cada valor do vetor menor ou igual a 10, escreva \"A[i] = x\", onde i é a posição do vetor e x é o valor armazenado na posição, com uma casa após o ponto decimal.")

    while True:
        vetor = [0] * 100
        for i in range(len(vetor)):
            vetor[i] = float(input())
        for i in range(len(vetor)):
            if vetor[i] <= 10:
                print(f"A[{i}] = {vetor[i]:.1f}")
        if input("Continuar Loop: 1 para continuar, 2 para sair") == "2": break
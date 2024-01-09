def ini1172():
    print("BEE 1172 - Substituição em Vetor I")
    print("Faça um programa que leia um vetor X[10]. Substitua a seguir, todos os valores nulos e negativos do vetor X por 1. Em seguida mostre o vetor X.")
    print("Entrada")
    print("A entrada contém 10 valores inteiros, podendo ser positivos ou negativos.")
    print("Saída")
    print ("Para cada posição do vetor, escreva \"X[i] = x\", onde i é a posição do vetor e x é o valor armazenado naquela posição.")
    while True:
        vetor = [1] * 10
        for i in range(len(vetor)):
            vetor[i] = int(input())
        if vetor[i] < 1:
            vetor[i] = 1
        for i in range(len(vetor)):
            print(f"X[{i}] = {vetor[i]}")
        if input("Continuar Loop: 1 para continuar, 2 para sair") == "2": break
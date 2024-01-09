from lib.interface import *
import lib.iniciante

opcoes = ['Básico - Beecrowd', 
          'String - Beecrowd', 
          'ADHOC - Beecrowd', 
          'Estrutura e Bibliotecas - Beecrowd', 
          'SQL - Beecrowd', 
          'Sair']


while True:
    resposta = menu([opcoes])
    if resposta == 1:
        break
    elif resposta == 2:
        break
    elif resposta == 3:
        break
    elif resposta == 4:
        break
    elif resposta == 5:
        break
    elif resposta == 6:
        print('Saindo do sistema ...')
        input('Precione enter para fechar.')
        break
    else:
        print('Erro! Digite uma opção válida')
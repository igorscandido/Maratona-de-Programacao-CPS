import sys

while True:

    entrada = input()

    if(entrada == "0"):
        break
    
    numeros = {
        0 : 0,
        1 : 0,
        2 : 0,
        3 : 0,
        4 : 0,
        5 : 0,
        6 : 0
    }

    dados = entrada.split(' ')

    for x in range(0,len(dados)):
        
        if(int(dados[x]) <= 9):
            numeros[0] += 1
        else:
            for j in range(1,7):
                if(int(dados[x][0]) == j):
                    numeros[j] += 1

    saida = ""

    for x in range(0,len(numeros)):
        
        if(numeros[x] != 0):
            saida += str(x) + ' ' + str(numeros[x]) + ' '

    print(saida)       

sys.exit()



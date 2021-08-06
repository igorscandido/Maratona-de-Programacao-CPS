import sys

while True:

    entrada = input()

    if(entrada == "0"):
        break

    dados = entrada.split(' ')

    altura_tijolo = int(dados[0])
    largura_tijolo = int(dados[1])
    comprimento_tijolo = int(dados[2])
    perimetro_comodo = int(dados[3])
    valor_milheiro = int(dados[4]) 


    area_comodo = perimetro_comodo * 2.8

    tamanho_tijolo = (altura_tijolo * largura_tijolo) / 100 #decimal

    tijolos_por_metro = int((1 / ( ( (comprimento_tijolo /100) + 0.01) * ( (altura_tijolo / 100) + 0.01) ) ))

    tijolos_pela_area = int(area_comodo * tijolos_por_metro)

    valor_pago = int((tijolos_pela_area / 1000) * valor_milheiro)


    print(str(tijolos_por_metro) + ' ' +
          str(tijolos_pela_area) + ' ' +
          str(valor_pago))


sys.exit()



import sys

while True:

    entrada = input()

    if (entrada == "0"):
        break

    if(entrada.find(';') < 0):
        cardeais = entrada.split(',')
    else:
        cardeais = entrada.split(';')

    latitude  = 0
    longitude = 0

    for x in range(0,len(cardeais)):

        aux = cardeais[x].split(' ')

        char = aux[0].find('º')

        graus = aux[0][:char]

        if(aux[1].find('’') > 0 or aux[1].find("'") > 0):
            
            char  = aux[1].find('’') or aux[1].find("'")

            minutos = float(aux[1][:char]) / 60

            char = aux[2].find('”') or aux[2].find('"')

            segundos = float(aux[2][:char]) / 3600

        else:

            char  = aux[2].find('’') or aux[2].find("'")

            minutos = float(aux[2][:char]) / 60

            char = aux[1].find('”') or aux[1].find('"')

            segundos = float(aux[1][:char]) / 3600

        if x == 0:
            latitude = float(graus) + minutos + segundos
        else:
            longitude = float(graus) + minutos + segundos
        
    
    output = ""

    if (latitude == 0):
        output += 'Equador '
    elif (latitude > 0):
        output += 'Norte '
    else:
        output += 'Sul '
    
    if (longitude == 0):
        output += 'Greenwich'
    elif (longitude > 0):
        output += 'Leste'
    else:
        output += 'Oeste'

    print(output)


sys.exit()
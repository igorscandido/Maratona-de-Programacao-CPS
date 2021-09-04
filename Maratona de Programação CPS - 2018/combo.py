import sys

while True:

    entrada = input()

    if (entrada == "0"):
        break

    cadeias = {
        3: 0,
        4: 0,
        5: 0
    }

    atual = entrada[0]
    sequencia = 1

    for x in range(1,len(entrada)):

        if (entrada[x] == atual):
            sequencia += 1
        else:
            atual = entrada[x]

            if (sequencia == 3):
                cadeias[3] += 1
            if (sequencia == 4):
                cadeias[4] += 1
            if(sequencia == 5):
                cadeias[5] += 1

            sequencia = 1
    
    if (sequencia == 3):
        cadeias[3] += 1
    if (sequencia == 4):
        cadeias[4] += 1
    if(sequencia == 5):
        cadeias[5] += 1

    valor = (10 * cadeias[3]) + (30 * cadeias[4]) + (50 * cadeias[5])

    print(valor)

sys.exit()
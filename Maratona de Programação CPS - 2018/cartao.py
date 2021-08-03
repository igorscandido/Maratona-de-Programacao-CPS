import sys

while True:

    entrada = input()

    if(entrada == "0"):
        break
    
    gabarito     = entrada.split(' ')[0]
    numero_alunos = entrada.split(' ')[1]

    desempenho_alunos = []

    for x in range(0,int(numero_alunos)):

        entrada_aluno      = input()
        respostas_certas   = 0

        for j in range(0,10):

            if (entrada_aluno[j] == gabarito[j]):
                respostas_certas += 1

        desempenho_alunos.append(
            [
                respostas_certas,
                str(respostas_certas) + '0',
                str(10 - respostas_certas) + '0'
            ]
        )

    
    for x in range(0, len(desempenho_alunos)):
        print(str(desempenho_alunos[x][0]) + ' ' + 
              str(desempenho_alunos[x][1]) + ' ' + 
              str(desempenho_alunos[x][2]))
    

    

sys.exit()

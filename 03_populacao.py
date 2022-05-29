populacao_A = int(input())   #TRANSFERI PRA UMA OUTRA VARIAVEL. PRA Q EU PUDESSE TRABALHAR SEMPRE COM O MAIOR RESULTADO, INDEPENDENTE SE ERA O PRIMEIRO OU SEGUNDO INPUT.
populacao_B = int(input())
populacao_MAIOR = 0
populacao_MENOR = 0
ano = 0  ##VOU REPETIR SÓ O TEMPO. LAÇO DE REPETIÇÃO. E A QUANTIDADE DE PESSOAS Q NASCEM. (2 E 3% NATALIDADE)

if populacao_A > populacao_B:
  populacao_MAIOR = populacao_A
  populacao_MENOR = populacao_B
else:
  populacao_MAIOR = populacao_B
  populacao_MENOR = populacao_A

while populacao_MAIOR > populacao_MENOR:   #SÓ BOTO NO LAÇO DE REPETIÇAO AS VARIAVEIS
                                            #QUE VAO SER MUDADAS COM O PASSAR DO TEMPO.
  ano += 1
  populacao_MAIOR += (2/100)*populacao_MAIOR
  populacao_MENOR += (3/100)*populacao_MENOR

print(ano)

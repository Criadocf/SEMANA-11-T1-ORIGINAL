populacao_inicial = int(input())
ano = 1600
nascidos_no_ano = 0
mortes_no_ano = 0
populacao_atual = populacao_inicial

while populacao_inicial >= (10/100)*populacao_atual:
  mortes_no_ano = (6/100)*populacao_inicial
  nascidos_no_ano = (1/100)*(populacao_inicial)

  populacao_inicial -= mortes_no_ano
  populacao_inicial += nascidos_no_ano
  
  
  print(f'{ano:.0f},{nascidos_no_ano:.0f},{mortes_no_ano:.0f},{populacao_inicial:.0f}')
  ano += 1
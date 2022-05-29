metros_a_frente_tartaruga = int(input())
metros_lebre = 0
metros_tartaruga = metros_a_frente_tartaruga
minuto = 0

while metros_lebre < metros_tartaruga:
    minuto += 1
    metros_lebre += 10
    metros_tartaruga += 1
print(minuto)
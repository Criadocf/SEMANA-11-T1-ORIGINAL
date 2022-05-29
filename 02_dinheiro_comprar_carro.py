dinheiro_no_bolso = 10000
preco_da_nave = float(input())
mes = 0

while dinheiro_no_bolso < preco_da_nave:
    dinheiro_no_bolso += (0.7/100)*dinheiro_no_bolso
    preco_da_nave += (0.4/100)*preco_da_nave
    mes += 1
print(mes)
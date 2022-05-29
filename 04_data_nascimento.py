nascimento = int(input())
oitavo = nascimento % 10
setimo = (nascimento % 100) // 10
sexto = ((nascimento // 100) % 100) % 10
quinto = ((nascimento // 100) % 100) // 10
quarto = (((nascimento/10000) % 10)*10)//10
terceiro = ((nascimento/10000) % 100)//10
segundo = ((nascimento/10000) % 1000)//100
primeiro = (nascimento/100000)//100

print(f'{oitavo+setimo+sexto+quinto+quarto+terceiro+segundo+primeiro:.0f}')

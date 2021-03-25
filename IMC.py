nome = 'Victor'
idade = 33
altura = 1.72
e_maior = idade>18
peso = 94
imc = peso/(altura**2)
condicao_1 = 'Baixo Peso'  # 18
condicao_2 = 'Peso Normal'  # 18.1 - 24.9
condicao_3 = 'Pré Obesidade'  # 25 - 29.9
condicao_4 = 'Obesidade Grau I'  # 30 - 34.9
condicao_5 = 'Obesidade Grau II'  # 35 - 39.9
condicao_6 = 'Obesidade Grau III'  # 40
print('Nome:', nome)
print('Idade:', idade)
print('Altura:', altura)
print('É maior de idade?', e_maior)
print('Peso:', peso)
print(nome, 'tem', idade, 'anos de idade e seu imc é', int(imc))
if imc < 18:
 print('Condição:', condicao_1)
elif imc < 25:
  print('Condição:', condicao_2)
elif imc < 29:
  print('Condição:', condicao_3)
elif imc < 35:
  print('Condição:', condicao_4)
elif imc < 40:
  print('Condição:', condicao_5)
elif imc > 40:
  print('Condição:', condicao_6)

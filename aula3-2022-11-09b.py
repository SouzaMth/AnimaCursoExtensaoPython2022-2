#funcoes

preco = 19.90

imposto = preco * 0.05
print(imposto)

preco2 = 100
imposto2 = preco2 * 0.05
print(imposto2)

#criar funcao calcularImposto() que calcula um imposto de 5% e retorna a quem pediu
def calcularImposto(preco):
  imposto = preco * 0.07
  return imposto

preco = 299
imposto = calcularImposto(preco)
print(imposto)

valores = [1.99, 24.50, 78.27, 1515.50]
#se eu quiser calcular o imposto destes quatro valores
for valor in valores:
  print("O imposto de {} é {}".format(valor, calcularImposto(valor)))

#declarar uma funcao calcularImpostoAliquota que recebe dois parametros: o preco do produto e a aliquota de imposto a ser aplicada e retorna o imposto calculado. Se a aliquota nao for informada, utilize 7% como padrao
def calcularImpostoAliquota(valor, aliquota = 7):
  imposto = valor * (aliquota /100)
  return imposto

print("\n")
for valor in valores:
  print("O imposto de {} é {}".format(valor, calcularImpostoAliquota(valor, 12)))
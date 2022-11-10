#Aula 26-10

#comando input(): permite o usuario digitar algo

nome = input("Digite seu nome: ")

idade = int(input("Digite a sua idade: "))

sexo = input("Informe seu sexo? (M ou F): ")

print("Boa noite, seu nome é {}".format(nome))
print("Sua idade é {}".format(idade))

#dobro da idade
dobro = idade * 2
print("O dobro da idade informada é {}".format(dobro))

#condicional
if idade >= 18:
  print("Voce ja e maior de idade! Já pode beber ou dirigir")
else:
  print("Voce é jovem ainda")

#E se eu quisesse perguntar o gênero (M = Masculino e F = Feminino)
#Mostre (...e você também precisa/precisou prestar o serviço militar obrigatório)
if idade >= 18 and sexo == 'M':
  print("Voce também deve prestar serviço militar")
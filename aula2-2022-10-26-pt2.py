#Aula 26-10
 #Pede o nome do aluno e sua nota (de 0 a 10) e, se ele tirou nota 10, mostra "Voce é o bichao, mesmo..."

nome = input("Informe seu nome: ")
nota = float(input("Informe sua nota (de 0 a 10): "))

print("Seu nome é {} e tirou {}".format(nome, nota))
if nota == 10:
  print("Voce é o bichao, mesmo...")
elif 6 <= nota <= 10:
  print("Bom trabalho")
else:
  print("Burro, não tirou dez...")
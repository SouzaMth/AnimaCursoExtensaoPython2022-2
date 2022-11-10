#Aula 09-11-22

contador = 1
while (contador <= 10):
  print(contador)
  contador += 1

#laço for (em phython, for = for each)
fruta = "morango"
print(fruta)

fruta1 = "morango"
fruta2 = "laranja"
fruta3 = "pera"

#lista
frutas = ["morango", "laranja", "pera"]
print(frutas[2])

print(len(frutas))

#add fruta nova
frutas.append("manga")

print(len(frutas))
print(frutas)

#while
i = 0
while(i < len(frutas)):
  print(frutas[i])
  i += 1

#exibir frutas com for
print("Exemplo de frutas com FOR")
for fruta in frutas:
  print(fruta)
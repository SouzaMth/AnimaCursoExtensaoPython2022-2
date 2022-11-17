import aula4_2022_11_16c as bd

conexao, cursor = bd.conectar()

nome = input("Digite o nome do herói/vilão: ")
nome_civil = input("Informe o nome civil do heroi/vilao (sua identidade secreta): ")
tipo_numerico = input("Tecle 1 para heroi ou 2 para vilao: ")

#consulta para o valor maximo usado no banco
sql = "SELECT MAX(pessoa_id)+1 FROM pessoas"
cursor.execute(sql)
pessoa_id = cursor.fetchone()[0]

if tipo_numerico == "1":
  tipo = "Herói(na)"
else:
  tipo = "Vilã(o)"

sql = f"INSERT INTO pessoas (pessoa_id, nome, nome_civil, tipo) VALUES ({pessoa_id}, '{nome}', '{nome_civil}', '{tipo}')"

cursor.execute(sql)
conexao.commit()
conexao.close()
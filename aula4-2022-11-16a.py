#1o. passo: importar a biblioteca sqlite3
import sqlite3

#2o. passo: estabelecer conexao com o banco de dados
conexao = sqlite3.connect("dc_universe.db")

#3o. passo: criar um objeto do tipo cursor
cursor = conexao.cursor()

#4o. passo: comando sql no banco
sql = "SELECT pessoa_id, nome, nome_civil, tipo FROM pessoas"

#5o. passo: executar o comando SQL no SQLite (no cursor)
cursor.execute(sql)

#6o. passo: exibir a consulta com todos os nomes de herois e viloes do banco de dados
pessoas = cursor.fetchall()
for pessoa in pessoas:
  print(pessoa)

for pessoa in pessoas:
  print("Nome: {} ({})".format(pessoa[1], pessoa[3]))
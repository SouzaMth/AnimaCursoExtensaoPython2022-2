#1o. passo: importar a biblioteca sqlite3
import sqlite3

#2o. passo: estabelecer conexao com o banco de dados
conexao = sqlite3.connect("dc_universe.db")

#3o. passo: criar um objeto do tipo cursor
cursor = conexao.cursor()

#4o. passo: comando para inserir um heroi/vilao
sql = "INSERT INTO pessoas (pessoa_id, nome, nome_civil, tipo) VALUES (12,'The Flash', 'Barry Allen', 'Herói(na)')"

#5o. passo: executar o comando SQL
cursor.execute(sql)

#6o. passo: confirmar alteração no banco de dados e fecha-lo
conexao.commit()
conexao.close()

print("Ok")
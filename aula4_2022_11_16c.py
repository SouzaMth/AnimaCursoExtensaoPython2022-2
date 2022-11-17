#1o. passo: importar a biblioteca sqlite3
import sqlite3

#passos 2 e 3 virarao funcao conectar()
def conectar():
  #2o. passo: estabelecer conexao com o banco de dados
  conexao = sqlite3.connect("dc_universe.db")

  #3o. passo: criar um objeto do tipo cursor
  cursor = conexao.cursor()

  return conexao, cursor

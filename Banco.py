import mysql.connector

class Banco():
    def init(self):
        self.conexao = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="joaosantos_db"
        )
        self.create.Table()
    def createTable(self):
        c = self.conexao.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS tb_usuario (id_usuario INT NOT NULL AUTO INCREMENT PRIMARY KEY,
         nm_usuario VARCHAR(45) NOT NULL,
         telefone VARCHAR(11),
         email VARCHAR(45),
         usuario VARCHAR(45)
         senha VARCHAR(45)) ''')

        self.conexao.commit()
        c.close()
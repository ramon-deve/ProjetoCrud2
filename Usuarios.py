import mysql.connector
from Banco import Banco

class Usuarios(object):
    def init(self,id_usuario=0,nm_usuario="",telefone="",email="",usuario="",senha=""):
        self.info = {}
        self.idusuario = id_usuario
        self.nome = nm_usuario
        self.telefone = telefone
        self.email = email
        self.usuario = usuario
        self.senha = senha

    def insertUser(self):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("INSERT INTO tb_usuario(nm_usuario, telefone, email, usuario, senha) VALUES(%s, %s, %s, %s, %s)",
                                                     (self.nome,self.telefone,self.email,self.usuario,self.senha))
            banco.conexao.commit()
            c.close
            return "Usuário cadastrado com sucesso"

        except Exception as e:
            return f"Ocorreu um erro na inserção de usuário: {e}"

    def updateUser(self):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("UPDATE tb_usuario SET nm_usuario = %s, telefone = %s, email = %s, usuario = %s, senha = %s WHERE id_usuario = %s",
                                        (self.nome,self.telefone,self.email,self.usuario,self.senha,self.idusuario))
            banco.conexao.commit()
            c.close
            return "Usuário alterado com sucesso"

        except Exception as e:
            return f"Ocorreu um erro na alteração do usuário"
from Usuarios import Usuarios
from tkinter import *
import mysql.connector

class Application:

    def __init__(self,master=None):
       self.fonte=("Verdana","8")

       self.container1 = Frame(master)
       self.container1["pady"]=10
       self.container1.pack()

       self.container2 = Frame(master)
       self.container2["padx"]=20
       self.container2["pady"]=5
       self.container2.pack()

       self.container3 = Frame(master)
       self.container3["padx"]=20
       self.container3["pady"]=5
       self.container3.pack()

       self.container4 = Frame(master)
       self.container4["padx"]=20
       self.container4["pady"]=5
       self.container4.pack()

       self.container5 = Frame(master)
       self.container5["padx"]=20
       self.container5["pady"]=5
       self.container5.pack()

       self.container6 = Frame(master)
       self.container6["padx"]=20
       self.container6["pady"]=5
       self.container6.pack()

       self.container7 = Frame(master)
       self.container7["padx"]=20
       self.container7["pady"]=5
       self.container7.pack()

       self.container8 = Frame(master)
       self.container8["padx"]=20
       self.container8["pady"]=10
       self.container8.pack()

       self.container9 = Frame(master)
       self.container9["pady"]=15
       self.container9.pack()

       self.titulo = Label(self.container1,text="Informe os dados: ")
       self.titulo["front"] = ("Calibri","9","bold")
       self.titulo.pack()

       self.lblidusuario = Label(self.container2,text="IDUsuario: ",font=self.fonte,width=10)
       self.lblidusuario.pack(side=LEFT)

       self.txtidusuario = Entry(self.container2)
       self.txtidusuario["width"]=10
       self.txtidusuario["front"]=self.fonte
       self.txtidusuario.pack(side=LEFT)

       self.btnBuscar = Button(self.container2,text="Buscar",font=self.fonte,width=10)
       self.btnBuscar["command"]=self.buscarUsuario
       self.btnBuscar.pack(side=RIGHT)

       self.lblnome = Label(self.container3,text="Nome: ",font=self.fonte,width=10)
       self.lblnome.pack(side=LEFT)

       self.txtnome = Entry(self.container3)
       self.txtnome["width"]=25
       self.txtnome["front"]=self.fonte
       self.txtnome.pack(side=LEFT)

       self.lbltelefone = Label(self.container4,text="Telefone: ",font=self.fonte,width=10)
       self.lbltelefone.pack(side=LEFT)

       self.txttelefone = Entry(self.container4)
       self.txttelefone["width"]=25
       self.txttelefone["front"]=self.fonte
       self.txttelefone.pack(side=LEFT)

       self.lblemail = Label(self.container5,text="Email: ",font=self.fonte,width=10)
       self.lblemail.pack(side=LEFT)

       self.txtemail = Entry(self.container5)
       self.txtemail["width"]=25
       self.txtemail["front"]=self.fonte
       self.txtemail.pack(side=LEFT)

       self.lblusuario = Label(self.container6,text="Usuario: ",font=self.fonte,width=10)
       self.lblusuario.pack(side=LEFT)

       self.txtusuario = Entry(self.container6)
       self.txtusuario["width"]=25
       self.txtusuario["front"]=self.fonte
       self.txtusuario.pack(side=LEFT)

       self.lblsenha = Label(self.container7,text="Senha: ",font=self.fonte,width=10)
       self.lblsenha.pack(side=LEFT)
       self.txtsenha = Entry(self.container7)
       self.txtsenha["width"]=25
       self.txtsenha["show"]="*"
       self.txtsenha["font"]=self.fonte
       self.txtsenha.pack(side=LEFT)
       
       self.bntInsert = Button(self.container8,text="Inserir",font=self.fonte,width=12)
       self.bntInsert["command"]= self.insertUsuario
       self.bntInsert.pack(side=LEFT)

       self.bntAlterar = Button(self.container8,text="Alterar",font=self.fonte,width=12)
       self.bntAlterar["command"]= self.alterarUsuario
       self.bntAlterar.pack(side=LEFT)

       self.bntExcluir = Button(self.container8,text="Excluir",font=self.fonte,width=12)
       self.bntExcluir["command"]= self.excluirUsuario
       self.bntExcluir.pack(side=LEFT)

       self.bntLimpar = Button(self.container8,text="Limpar",font=self.fonte,width=12)
       self.bntLimpar["command"]= self.limparCampos
       self.bntLimpar.pack(side=LEFT)

       self.lblmsg = Label(self.container9,text="")
       self.lblmsg["font"] = ("Verdana","9","italic")
       self.lblmsg.pack()

       self.conectarBanco()

    def conectarBanco(self):
       self.conn = mysql.connector.connect(
          host = "localhost",
          user = "root",
          password = "root",
          database =  "ramon_benites_db"
        )
       self.cursor = self.conn.cursor()
       self.cursor.execute('''CREATE TABLE IF NOT EXISTS tb_usuario(id_usuario INT NOT NULL AUTO INCREMENT PRIMARY KEY,
       nm_usuario VARCHAR(45) NOT NULL
       telefone VARCHAR(11),
       email VARCHAR(45),
       usuario VARChAR(45),
       senha VARCHAR(45)),''')

       self.conn.commit()
    
    def inserirUsuario(self):
        nome = self.txtnome.get()
        telefone = self.txttelefone.get()
        email = self.txtemail.get()
        usuario = self.txtidusuario.get()
        senha = self.txtsenha.get()
        self.cursor.execute("INSERT INTO tb_usuario(nm_nome,telefone,usuario,senha)VALUES(%s,%s,%s,%s,%s)",
                                                (nome,telefone,email,usuario,senha))
                                                                            

        self.conn.commit()
        self.lblmsg["text"]="Usuario Inserido com sucesso"
        self.limparCampos
    
    def alterarUsuario(self):
        nome = self.txtnome.get()
        telefone = self.txttelefone.get()
        email = self.txtemail.get()
        usuario = self.txtidusuario.get()
        senha = self.txtsenha.get()
        self.cursor.execute("UPDATE tb_usuario SET nm_usuario = %s, telefone = %s, email = %s, usuario = %s, senha = %s, WHERE id_usuario = %s",
        (nome,telefone,email,usuario,senha))

        self.conn.commit()
        self.lblmsg["text"]="Usuario alterado com sucesso"
        self.limparCampos()

    def excluirUsuario(self):
        id_usuario = self.txtidusuario.get()
        self.cursor.execute("DELETE FROM tb_usuario WHERE id_usuario = %s",(id_usuario,))
        self.conn.commit()
        self.lblmsg["text"]= " Usuario Excluido com sucesso "
        self.limparCampos()
    
    def buscarUsuario(self):
        id_usuario = self.txtidusuario.get()
        self.cursor.execute("Select * FROM tb_usuario WHERE id_usuario = %s",(id_usuario,))
        usuario = self.cursor.fetchone()

        if usuario:
            self.txtnome.insert(0,usuario[1])
            self.txttelefone.insert(0,usuario[2]) 
            self.txtemail.insert(0,usuario[3]) 
            self.txtusuario.insert(0,usuario[4]) 
            self.txtsenha.insert(0,usuario[5])  
        else:
            self.lblmsg["text"] = "Usuario não encontrado"
            self.limparCampos()

    def limparCampos(self): 
        self.txtnome.delete(0,END)
        self.txttelefone.delete(0,END) 
        self.txtemail.delete(0,END)
        self.txtusuario.delete(0,END)
        self.txtsenha.delete(0,END)

    def __del__(self):
        self.conn.close()











if __name__=="__main_":
    root = Tk()
    Application(root)
    root.mainloop()
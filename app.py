from tkinter import *
from Packages.dados import Registrados

class Aplication:
    def __init__(self, master = None):
        self.fonte = ("Arial", "10")

        self.primeiro_conteiner = Frame(master)
        self.primeiro_conteiner["pady"] = 10
        self.primeiro_conteiner.pack()

        self.segundo_container = Frame(master)
        self.segundo_container["pady"] = 10
        self.segundo_container.pack()

        self.terceiro_container = Frame(master)
        self.terceiro_container["pady"] = 10
        self.terceiro_container.pack()

        self.quarto_container = Frame(master)
        self.quarto_container["pady"] = 10
        self.quarto_container.pack()        

        self.titulo = Label(self.primeiro_conteiner)
        self.titulo["text"] = "DADOS"
        self.titulo["font"] = ("Arial", "10", "bold")
        self.titulo.pack()

        self.label_cpf = Label(self.segundo_container)
        self.label_cpf["text"] = "CPF"
        self.label_cpf["font"] = self.fonte
        self.label_cpf.pack(side=LEFT)

        self.cpf = Entry(self.segundo_container)
        self.cpf["width"] = 30
        self.cpf.pack(side=LEFT)

        self.label_senha = Label(self.terceiro_container)
        self.label_senha["text"] = "Senha"
        self.label_senha["font"] = self.fonte
        self.label_senha.pack(side=LEFT)

        self.senha = Entry(self.terceiro_container)
        self.senha["width"] = 30
        self.senha["show"] = "*"
        self.senha.pack(side=LEFT)

        self.botao = Button(self.quarto_container)
        self.botao["text"] = "Enviar"
        self.botao["width"] = 5
        self.botao["font"] = ("Calibri", "8")
        self.botao["command"] = self.Verificar
        self.botao.pack()

        self.texto = Label(self.quarto_container, text="", font=self.fonte)
        self.texto.pack()    


    def Verificar(self):
        cpf = self.cpf.get()
        senha = self.senha.get()
        tabela = Registrados.registrados
        dicionario = {}
        for i in tabela.index:
            cpf_registrados = str(tabela.at[i, "CPF"])
            senha_registrados = str(tabela.at[i, "Password"])
            dicionario.update({cpf_registrados: senha_registrados})
    
        if senha == "" or cpf == "":
            self.texto["text"] = "Não autenticado"
            return
        
        elif cpf not in dicionario.keys():
            self.texto["text"] = "Não autenticado"
            return

        elif dicionario[cpf] == senha:
            self.texto["text"] = "Autenticado"

        else:
            self.texto["text"] = "Não autenticado"
    
root = Tk()
Aplication(root)
root.mainloop()
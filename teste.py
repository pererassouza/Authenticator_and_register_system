from dados import Registrados
import pandas as pd

def Organizar():
    tabela = pd.read_excel("Dados\\clientes_registrados.xlsx")

    for i in tabela.index:
        senha = tabela.at[i, "Password"]
        cpf = tabela.at[i, "CPF"]
        print(cpf, senha)
        print("=================================")



Organizar()
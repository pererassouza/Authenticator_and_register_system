import os
# from clients import Clients
from Script_Clients.clients import Clients
import random
import pandas as pd
class Registro(Clients):
    def __init__(self):
        os.system("cls")
        logger =False

        clients = pd.read_excel(r"Dados\clientes.xlsx")
        registred_clients = pd.read_excel(r"Dados\clientes_registrados.xlsx") 

        def criar_senha():
            senha = ''
            for i in range(4):
                senha += str(random.randint(0,9,))
            return senha

        clientes  =[]
        for linha, coluna in clients.iterrows():
            name = coluna["Name"]
            middlename = coluna["Middlename"]
            age = coluna["Age"]
            cpf = str(coluna["CPF"])
            heigth = coluna["Height"]
            rg = coluna["RG"]
            
            if cpf not in str(registred_clients["CPF"]):        

                cliente = Clients(name= name, middlename= middlename, age=age, cpf=cpf, height=heigth, rg=rg)
                clientes.append(cliente)   
                cliente.authentication_client

                if cliente.logger():
                    logger = True
                else:
                    logger = False

                if logger:
                    
                    nova_linha = {"Name": name, "Middlename": middlename, "Age": int(age), "Height": float(heigth), "CPF": int(cpf), "RG": int(rg), "Password": criar_senha()}
                    registred_clients = registred_clients._append(nova_linha, ignore_index=True)
                    registred_clients.drop_duplicates(subset=["CPF"], keep="last", inplace = True)
                    registred_clients.to_excel(r"Dados\clientes_registrados.xlsx",sheet_name="teste",index = False)

            else:
                print(f"{name} {middlename} duplicated cpf!")
                msg = f"{name} {middlename} registration failed! (Duplicated CPF)\n"
                self._log_failure(msg)
Registro()


    # registred_clients = pd.concat([registred_clients, novos_dados], ignore_index= True)

    # with pd.ExcelWriter("Teste.xlsx", engine="openpyxl", mode = "a") as writer:
    #     registred_clients.to_excel(writer, index =False)
    # # if logger:
    #     registred_clients["name"] = name
    #     registred_clients["Middlename"] = middlename
    #     registred_clients["Age"] = age
    #     registred_clients["CPF"] = cpf
    #     registred_clients.to_excel("Teste.xlsx", index = False)
    # registred_clients.save("teste.xlsx")
# registred_clients.close()



# name = clients["Name"].to_list()
# cpf = clients["CPF"].to_list()
# middlename = clients["Middlename"].to_list()
# age = clients["Age"].to_list()
# teste = {"name": name, "middlename": middlename, "age": age, "cpf": cpf}

# mark_ = Clients("Mark")
# mark_.middlename = "Jhon"
# mark_.age = 24
# mark_.height = 1.83
# mark_.cpf = "23864088844"
# mark_.rg = "552376632"

# daphine_ =  Clients("Daphine")
# daphine_.middlename = "Smith"
# daphine_.age = 17
# daphine_.height = 1.64
# daphine_.cpf = "39446860806"
# daphine_.rg = "478930983"

# mary_ =  Clients("Mary")
# mary_.middlename = "Cury"
# mary_.age = 15
# mary_.height = 1.63
# mary_.cpf = "23908637100"
# mary_.rg = "729037623"

# chloe_ =  Clients("Chloe")
# chloe_.middlename = "Borjuar"
# chloe_.age = 20
# chloe_.height = 1.61
# chloe_.cpf = "11350590800"
# chloe_.rg = "248910024"

# billy_ =  Clients("Billy")
# billy_.middlename = "Jeans"
# billy_.age = 119
# billy_.height = 1.90
# billy_.cpf = "23156783088"
# billy_.rg = "248910024"


# mark_.authentication_client
# daphine_.authentication_client
# mary_.authentication_client
# chloe_.authentication_client    
# billy_.authentication_client

# mark_.logger()
# mary_.logger()
# daphine_.logger()
# chloe_.logger()
# billy_.logger()

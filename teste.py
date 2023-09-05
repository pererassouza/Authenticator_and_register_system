import pandas as pd

clientes = pd.read_excel("clientes.xlsx")

name = clientes["Name"].to_list()

print(name)

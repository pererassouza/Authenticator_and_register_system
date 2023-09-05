duplicated_cpf =False
invalid_cpf = False
is_minor = False
not_auth = False

valores  =[duplicated_cpf, invalid_cpf, is_minor, not_auth]
values = {
    duplicated_cpf: print( f"registration failed! (Duplicated CPF)\n"),
    invalid_cpf: print(f" registration failed! (Invalid cpf)\n"),
    is_minor: print(f"registration failed! (Is Minor)\n"),
    not_auth: print(f"registration failed! (Not Authenticated)\n")
}

for i in valores:
    if i in values and i is True:
       i()
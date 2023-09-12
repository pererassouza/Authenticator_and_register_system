# from cpf_validation import Verificador
from Packages.cpf_validation import Verificador
class People():
    def __init__(self, name, middlename, age, cpf,height, rg) -> None:
        self.name = name
        self.middlename = middlename
        self.age = age
        self.height = height
        self.cpf = cpf
        self.rg = rg
        self.duplicated_cpf = False

    @property 
    def show_people(self):
        print(f'''    -Name: {self.name } {self.middlename}
    -Age: {self.age}
    -Height: {self.height}
    -cpf: {self.cpf}
    -rg: {self.rg}\n''')

    def _verificar_cpf(self):
        if self.cpf not in Verificador.list_of_cpf:
            cpf = Verificador(self.cpf)  
            self.duplicated_cpf = False      
            return cpf.verificar_cpf()
        else:
            self.duplicated_cpf = True
            # return
    

# mark_ = People("Mark")
# mark_.middlename = "Jhon"
# mark_.age = 25
# mark_.height = 1.83
# mark_.cpf = "238640888"
# mark_.rg = "552376632"
# mark_._verificar_cpf()





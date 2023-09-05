# from people import People
# from log import LogFile
from Script_Clients.people import People
from Script_Clients.log import LogFile

class Clients(People, LogFile):
    def __init__(self, name, middlename, age, cpf, height, rg) -> None:
        super().__init__(name, middlename, age, cpf, height, rg)
        self.auth = False
        self.true_cpf = False    
        self.invalid_cpf =False
        self.minor = False     
        
    @property
    def authentication_client(self):
        if not self._verificar_cpf():
            if self.duplicated_cpf :
                print(f"{self.name} {self.middlename} duplicated cpf!")
                self.invalid_cpf = True
                return
            print(f"{self.name} {self.middlename} invalid cpf!")
            self.invalid_cpf = True
            return self.invalid_cpf
        if self.age < 18:
            print(f"{self.name} {self.middlename} is minor and are not allowed!")
            self.minor = True
            return self.minor
        print(f"{self.name} {self.middlename} successfully authenticated!")
        self.auth = True

    # @property    
    def logger(self):
        # self.authentication_client
        if self.auth:
            msg = f"{self.name} {self.middlename} successfully registered!\n"
            self._log_success(msg)
            return True

        if not self.auth:
            if self.invalid_cpf and self.duplicated_cpf:
                msg = f"{self.name} {self.middlename} registration failed! (Duplicated CPF)\n"
                self._log_failure(msg)
                return False
            elif self.invalid_cpf and not self.duplicated_cpf:
                msg = f"{self.name} {self.middlename} registration failed! (Invalid cpf)\n"
                self._log_failure(msg)
                return
            elif self.minor:
                msg = f"{self.name} {self.middlename} registration failed! (Is Minor)\n"
                self._log_failure(msg)
                return False
            else:
                msg = f"{self.name} {self.middlename} registration failed! (Not Authenticated)\n"
                self._log_failure(msg)  
                return False         


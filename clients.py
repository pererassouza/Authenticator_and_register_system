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
            duplicated_cpf = self.invalid_cpf and self.duplicated_cpf
            invalid_cpf = self.invalid_cpf and not self.duplicated_cpf
            is_minor = self.minor
            not_auth = self.auth

            # booll = [duplicated_cpf, invalid_cpf, is_minor, not_auth]

            # values = {
            #     duplicated_cpf: self._log_failure,
            #     invalid_cpf: self._log_failure,
            #     is_minor: self._log_failure,
            #     not_auth: self._log_failure
            # }
            # for i in booll:
            #     if i in values and i is True:
            #         i(f"{self.name} {self.middlename} registration failed! (Duplicated CPF)\n")


            if duplicated_cpf:
                msg = f"{self.name} {self.middlename} registration failed! (Duplicated CPF)\n"
                self._log_failure(msg)
                return False
            elif invalid_cpf:
                msg = f"{self.name} {self.middlename} registration failed! (Invalid cpf)\n"
                self._log_failure(msg)
                return
            elif is_minor:
                msg = f"{self.name} {self.middlename} registration failed! (Is Minor)\n"
                self._log_failure(msg)
                return False
            elif not_auth:
                msg = f"{self.name} {self.middlename} registration failed! (Not Authenticated)\n"
                self._log_failure(msg)  
                return False         

# c1 = Clients("das", "das" , "das", "23864088844", "dsa", "das")
# c1.authentication_client
# c1.logger()
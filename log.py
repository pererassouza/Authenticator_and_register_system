import datetime as dt
agora = dt.datetime.now()
agora_str = agora.strftime('%d/ %m/ %Y %H:%M')
data = agora.strftime('%d/ %m/ %Y')
hora = agora.strftime('%H:%M')

class Log:
    def _log(self, msg):  
        raise NotImplementedError ("Implemente o metodo log!")
    
    def _log_success(self, msg):
        return self._log(f"Succsess: {msg}")    
    
    def _log_failure(self, msg):
        return self._log(f"Failure: {msg}")

class LogFile(Log):
    def _log(self, msg):
        _msg = f"{msg}"
        print("Salving on log => ", _msg, "=====================================\n")
        with open("log.txt", "a") as arquivo:
            arquivo.write(f"{_msg}  => {agora_str}\n")
            arquivo.write("\n")

if __name__ == "__main__":
    lf = LogFile()
    lf._log("Teste")


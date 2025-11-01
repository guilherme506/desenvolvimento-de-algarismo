class conta:
    def __init__(self, titular, numero, saldo):
        self.saldo=0
        self.numero = numero
        self.titular = titular

        @property
        def saldo(self):
            return self. _saldo
        
        @saldo.setter
        def saldo(seld, saldo):
            if saldo<0:
                print("O saldo não pode ser negativo")
            else:
                self. _saldo = saldo
        
        def saque(self, valor):
            if self.saldo>=valor:
                self.saldo-=valor
                print("Saque realizado com sucesso")
            else:
                print("Saldo insuficente")
        

        def deposita(self,valor):
            self.saldo+=valor
        

        def extrato(self):
            print("cliente":,self._titular,"Saldo Atual",self._saldo)
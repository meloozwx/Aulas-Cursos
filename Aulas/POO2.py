class Conta:
    
    _quant = 0
    
    @classmethod
    def adiciona_conta(cls):
        cls._quant+=1
        
    @classmethod
    def quantidade(cls):
        return cls._quant
    
    def __init__(self, numero):
        self.adiciona_conta()
        self.numero = numero

contas = []

for i in range(0,9,1):
    conta = Conta(i)
    contas.append(conta)

print("Contas criadas: ", Conta.quantidade())
#
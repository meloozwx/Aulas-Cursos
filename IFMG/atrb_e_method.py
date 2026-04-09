class Conta:
    _quant = 0  # atributo de classe

    @classmethod
    def adiciona_conta(cls):
        cls._quant += 1

    @classmethod
    def quantidade(cls):
        return cls._quant

    def __init__(self, numero):
        self.numero = numero
        Conta.adiciona_conta()


# Teste do código
print('Contas criadas:', Conta.quantidade())

conta1 = Conta(1111)
print('Contas criadas:', Conta.quantidade())

conta2 = Conta(2222)
print('Contas criadas:', Conta.quantidade())
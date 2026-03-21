class Conta:
    def __init__(self, numero):
        self.numero = numero
        self._saldo = 0

    def depositar(self, valor):
        self._saldo += valor

    def saldo(self):
        return self._saldo

    def sacar(self, valor):
        if self._saldo >= valor:
            self._saldo -= valor
            return True
        else:
            return False


conta1 = Conta(1)
conta1.depositar(10)
print("Conta 1:", conta1.saldo())

conta2 = Conta(2)
conta2.depositar(250)
conta2.sacar(249)
print("Conta 2:", conta2.saldo())
###a#####
class Cliente:
    def __init__(self, nome, endereco):
        self._nome = nome
        self._endereco = endereco

    def imprime(self):
        print(
            'Cliente:', self._nome,
            '\nEndereço:', self._endereco
        )


class Conta:
    def __init__(self, numero, cliente):
        self._numero = numero
        self._saldo = 0
        self._cliente = cliente

    def depositar(self, valor):
        self._saldo += valor

    def imprime(self):
        print(
            'Conta:', str(self._numero),
            '\nSaldo:', str(self._saldo)
        )
        self._cliente.imprime()


# Uso do código
cliente = Cliente('Ana', 'Rua Um')
conta1 = Conta(1111, cliente)

cliente = Cliente('Loja X', 'Praça central')
conta2 = Conta(2222, cliente)

conta1.depositar(500.0)

conta1.imprime()
conta2.imprime()
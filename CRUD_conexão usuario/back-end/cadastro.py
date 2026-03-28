from db_usuarios import Database
from verificador_de_cpf import Verify

class Usuario():
    def conta(self, nome = None, senha = None, cpf = None):
        self.nome = nome
        self.senha = senha
        self.cpf = cpf
    
    def preencher():
        if not nome is None:
            nome = str(input("Digite seu nome: "))
        if not senha is None:
            senha = int(input("Digite sua senha (apenas números): "))
        if not cpf is None:
            cpf = int(input("Digite seu cpf: "))
            Verify.validar_cpf(cpf)

user1 = Usuario()
print(user1.preencher) 
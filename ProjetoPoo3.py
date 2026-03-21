class Emprego:
    def __init__(self, nome_emprego: str, salario: int) -> None:
        self.nome_emprego = nome_emprego
        self.salario = salario

    def apresentar(self) -> str:
        return f"Trabalhando como {self.nome_emprego} e ganhando R${self.salario}."


class Eletricista(Emprego):
    def __init__(self):
        super().__init__("Eletricista", 2500)

    def apresentar(self) -> str:
        return "Trabalhando ajeitando fios!!!"


class Programador(Emprego):
    def __init__(self):
        super().__init__("Programador", 3500)

    def apresentar(self) -> str:
        return "Trabalhando programando códigos!!!"


class Deputado(Emprego):
    def __init__(self):
        super().__init__("Deputado", 40000)

    def apresentar(self) -> str:
        return "Trabalhando como Deputado!!!"


class Pessoa:
    def __init__(self, nome: str, idade: int, emprego: Emprego):
        self.nome = nome
        self.idade = idade
        self.emprego = emprego

    def apresentar(self) -> str:
        return f"Olá, meu nome é {self.nome}, tenho {self.idade} anos. {self.emprego.apresentar()}"


def escolher_emprego():
    print("\nEscolha seu emprego:")
    print("1 - Eletricista")
    print("2 - Programador")
    print("3 - Deputado")

    while True:
        escolha = input("Digite o número do emprego: ")
        if escolha == "1":
            return Eletricista()
        elif escolha == "2":
            return Programador()
        elif escolha == "3":
            return Deputado()
        else:
            print("Opção inválida! Tente novamente...")
            return escolher_emprego()


if __name__== "__main__":
    print("=== CRIAÇÃO DE PERSONAGEM ===")
    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))
    emprego_escolhido = escolher_emprego()

    pessoa = Pessoa(nome, idade, emprego_escolhido)
    print(pessoa.apresentar())
###
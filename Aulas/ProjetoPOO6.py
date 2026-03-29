class Futebol:
    def __init__(self, nome=None, idade=None, posicao=None):
        if nome is None:
            nome = input("Qual seu nome? ")
        if idade is None:
            idade = input("Qual sua idade? ")
        if posicao is None:
            posicao = input(
                "Escolha uma posição:\n"
                "1 - Atacante\n"
                "2 - Meio Campo\n"
                "3 - Zagueiro\n"
                "Digite: "
            )

        self.nome = nome
        self.idade = idade
        self.posicao = posicao


class Atacante(Futebol):
    def __init__(self, nome=None, idade=None):
        super().__init__(nome, idade, "Atacante")
        print("Eu sou atacante e consigo chutar ao gol!")
        self.chutar = True


class MeioCampo(Futebol):
    def __init__(self, nome=None, idade=None):
        super().__init__(nome, idade, "Meio Campo")
        print("Eu sou meio campista e consigo fazer passes!")
        self.passar = True


class Zagueiro(Futebol):
    def __init__(self, nome=None, idade=None):
        super().__init__(nome, idade, "Zagueiro")
        print("Eu sou zagueiro e consigo defender chutes!")
        self.defender = True


def escolher_posicao():
    print("\nEscolha sua posição:")
    print("1 - Atacante")
    print("2 - Meio Campo")
    print("3 - Zagueiro")

    while True:
        escolha = input("Digite o número da posição: ")
        if escolha == "1":
            return Atacante()
        elif escolha == "2":
            return MeioCampo()
        elif escolha == "3":
            return Zagueiro()
        else:
            print("Opção inválida! Tente novamente...")


print("---- Monte seu Personagem ----")
p1 = escolher_posicao()
print(f"Meu nome é {p1.nome},tenho {p1.idade} anos e jogo na posição de {p1.posicao}!")

###
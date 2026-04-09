class Hotel:
    def _init_ (self, quarto=None, valor=None, cliente=None, numero=None, cor=None, comodos=None):
        self.quarto = quarto
        self.valor = valor
        self.cliente = cliente
        self.numero = numero
        self.comodos = comodos
        self.cor = cor
    def desc(self):
        self.numero = input("Qual o número da sua casa?")
        self.cor = input("Qual a cor do seu quarto?")
        self.comodos = input("Quantos comodos tem no seu quarto?")

        return(f"A sua casa é a {self.numero}, a cor de sua casa é {self.cor} e tem {self.comodos}")

h = Hotel()
print(h.desc())

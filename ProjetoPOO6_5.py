from Inimigo import Inimigo
class Pessoa:
    def __init__(self, nome = None, mana = None, idade = None):
        
        if nome is None:
            nome = input("Qual o nome do personagem? ")
        self.nome = nome
        if mana is None:
            mana = input("Qual a mana do personagem? ")
        self.mana = mana
        if idade is None:
            idade = int(input("Qual a idade do personagem? "))
        self.idade = idade

    def desc(self):
        return (f"O nome do personagem é {self.nome}, ele tem {self.mana} de mana e {self.idade} anos de idade.")
    
p = Pessoa()
print(p.desc())
######
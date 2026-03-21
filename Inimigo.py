class Inimigo:
    def __init__(self, nome = None, vida = None, ataque = None, defesa = None):
        if nome is None:
            nome = input("Qual o nome do inimigo? ")
            self.nome = nome
        if vida is None:
            vida = int(input("Qual a vida do inimigo? "))
            self.vida = vida
        if ataque is None:
            ataque = int(input("Qual o ataque do inimigo? "))
            self.ataque = ataque
        if defesa is None:
            defesa = int(input("Qual a defesa do inimigo? "))
            self.defesa = defesa
        
        def Hab(Inimigo):
            super().__init__(self, nome, vida, ataque, defesa)
        
        ######
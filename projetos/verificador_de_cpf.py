import re

class Verify():

    @staticmethod
    def validar_cpf(cpf: str) -> bool:
        # Remove tudo que não for número
        cpf = re.sub(r'\D', '', cpf)

        # Verifica tamanho
        if len(cpf) != 11:
            return False

        # Elimina CPFs com todos os números iguais (ex: 11111111111)
        if cpf == cpf[0] * 11:
            return False

        # -------- 1º dígito verificador --------
        soma = 0
        for i in range(9):
            soma += int(cpf[i]) * (10 - i)

        digito1 = (soma * 10) % 11
        if digito1 == 10:
            digito1 = 0

        if digito1 != int(cpf[9]):
            return False

        # -------- 2º dígito verificador --------
        soma = 0
        for i in range(10):
            soma += int(cpf[i]) * (11 - i)

        digito2 = (soma * 10) % 11
        if digito2 == 10:
            digito2 = 0

        if digito2 != int(cpf[10]):
            return False

        return True
import sys
sys.path.append("/home/joao/BTI/6º SEMESTRE/TS/fila-pronto-socorro/")

import unittest
from datetime import datetime
from main.error import ValidacaoError
from main.domain import Paciente, FilaAtendimento, Risco, Atendimento, FilaVaziaError, FichaAnalise

class TestPacientePaths(unittest.TestCase):
    """
    Cada teste abaixo segue um caminho específico (CT) no grafo da classe Paciente:
    
    Nós (em números):
    1: __post_init__
    2: validar_nome
    3: validar_cpf
    4: ValidacaoError(nome)
    5: validar_email
    6: ValidacaoError(cpf)
    7: validar_nascimento
    8: ValidacaoError(email)
    9: paciente criado com sucesso
    10: ValidacaoError(nascimento)

    Caminhos:
    CT1 = [1, 2, 3, 5, 7, 9]
    CT2 = [1, 2, 4]
    CT3 = [1, 2, 3, 6]
    CT4 = [1, 2, 3, 5, 8]
    CT5 = [1, 2, 3, 5, 7, 10]
    """

    def test_CT1(self):
        """
        CT1 = [1, 2, 3, 5, 7, 9]
        Fluxo: __post_init__ -> validar_nome(T) -> validar_cpf(T) ->
               validar_email(T) -> validar_nascimento(T) -> paciente criado com sucesso.
        
        Todos os dados são válidos. Deve chegar ao nó 9 (criado com sucesso).
        Não deve lançar exceção.
        """
        paciente = Paciente(
            nome="João",
            cpf="12345678901",
            email="valido@example.com",
            nascimento="01/01/2000"  # Data válida
        )

    def test_CT2(self):
        """
        CT2 = [1, 2, 4]
        Fluxo: __post_init__ -> validar_nome(F) -> ValidacaoError(nome).
        
        Nome inválido dispara ValidacaoError imediatamente (nó 4).
        """
        with self.assertRaises(ValidacaoError):
            Paciente(
                nome="",  # Inválido
                cpf="12345678901",
                email="valido@example.com",
                nascimento="01/01/2000"
            )

    def test_CT3(self):
        """
        CT3 = [1, 2, 3, 6]
        Fluxo: __post_init__ -> validar_nome(T) -> validar_cpf(F) -> ValidacaoError(cpf).
        
        Nome válido, mas CPF inválido gera exceção (nó 6).
        """
        with self.assertRaises(ValidacaoError):
            Paciente(
                nome="Pedro",
                cpf="cpf_invalido",  # Formato inválido
                email="valido@example.com",
                nascimento="01/01/2000"
            )

    def test_CT4(self):
        """
        CT4 = [1, 2, 3, 5, 8]
        Fluxo: __post_init__ -> validar_nome(T) -> validar_cpf(T) ->
               validar_email(F) -> ValidacaoError(email).
        
        Nome e CPF válidos, e-mail inválido gera exceção (nó 8).
        """
        with self.assertRaises(ValidacaoError):
            Paciente(
                nome="Maria",
                cpf="12345678901",
                email="invalido",  # Email inválido
                nascimento="01/01/2000"
            )

    def test_CT5(self):
        """
        CT5 = [1, 2, 3, 5, 7, 10]
        Fluxo: __post_init__ -> validar_nome(T) -> validar_cpf(T) ->
               validar_email(T) -> validar_nascimento(F) -> ValidacaoError(nascimento).
        
        Nome, CPF, e-mail válidos, mas data de nascimento inválida -> exceção (nó 10).
        """
        with self.assertRaises(ValidacaoError):
            Paciente(
                nome="José Maria",
                cpf="12345678901",
                email="valido@example.com",
                nascimento="32/01/2000"  # Data inválida
            )

if __name__ == '__main__':
    unittest.main()
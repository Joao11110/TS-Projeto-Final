import sys
sys.path.append("/home/joao/BTI/6º SEMESTRE/TS/fila-pronto-socorro/")

import unittest
from datetime import datetime
from main.error import ValidacaoError
from main.domain import Paciente, FilaAtendimento, Risco, Atendimento, FilaVaziaError, FichaAnalise

# --------------------------------------
# RF1: Registrar Paciente
# --------------------------------------

class TestRF1(unittest.TestCase):
    def test_registro_valido(self):
        paciente = Paciente(
            nome="Maria Silva",
            cpf="12345678909",
            email="maria@exemplo.com",
            nascimento="01/01/1990"
        )
        self.assertEqual(paciente.cpf, "12345678909")

    def test_registro_invalidos(self):
        casos = [
            ("111222333XX", "maria@exemplo.com", "01/01/1990", "CPF inválido"),
            ("12345678909", "mariaexemplo.com", "01/01/1990", "E-mail inválido"),
            ("12345678909", "maria@exemplo.com", "31/13/2020", "Data de nascimento inválida"),
        ]
        
        for cpf, email, nascimento, erro in casos:
            with self.subTest(cpf=cpf, email=email, nascimento=nascimento):
                with self.assertRaises(ValidacaoError) as cm:
                    Paciente(nome="Maria Silva", cpf=cpf, email=email, nascimento=nascimento)
                self.assertIn(erro, str(cm.exception))

if __name__ == '__main__':
    unittest.main(verbosity=2)
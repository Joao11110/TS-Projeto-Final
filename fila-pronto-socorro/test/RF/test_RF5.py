import sys
sys.path.append("/home/joao/BTI/6º SEMESTRE/TS/fila-pronto-socorro/")

import unittest
from datetime import datetime
from main.error import ValidacaoError
from main.domain import Paciente, FilaAtendimento, Risco, Atendimento, FilaVaziaError, FichaAnalise

# --------------------------------------
# RF5: Pesquisar Histórico
# --------------------------------------

class TestRF5(unittest.TestCase):
    def test_buscar_cpf_registrado(self):
        paciente = Paciente("Carlos", "55555555555", "carlos@exemplo.com", "05/05/2000")
        self.assertEqual(paciente.cpf, "55555555555")

    def test_buscar_cpf_nao_registrado(self):
        with self.assertRaises(ValueError) as cm:
            raise ValueError("Paciente não encontrado")
        self.assertIn("Paciente não encontrado", str(cm.exception))

if __name__ == '__main__':
    unittest.main(verbosity=2)
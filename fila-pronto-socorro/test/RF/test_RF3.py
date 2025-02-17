import sys
sys.path.append("/home/joao/BTI/6º SEMESTRE/TS/fila-pronto-socorro/")

import unittest
from datetime import datetime
from main.error import ValidacaoError
from main.domain import Paciente, FilaAtendimento, Risco, Atendimento, FilaVaziaError, FichaAnalise

# --------------------------------------
# RF3: Gerenciar Fila
# --------------------------------------

class TestRF3(unittest.TestCase):
    def setUp(self):
        self.fila = FilaAtendimento()

    def test_prioridade_maxima(self):
        paciente = Paciente("João", "11111111111", "joao@exemplo.com", "01/01/2000")
        self.fila.inserir(Atendimento(paciente, Risco.VERMELHO))
        self.assertEqual(self.fila.proximo().risco, Risco.VERMELHO)

    def test_mesma_prioridade(self):
        paciente1 = Paciente("Ana", "22222222222", "ana@exemplo.com", "02/02/2000")
        paciente2 = Paciente("Pedro", "33333333333", "pedro@exemplo.com", "03/03/2000")
        self.fila.inserir(Atendimento(paciente1, Risco.LARANJA))
        self.fila.inserir(Atendimento(paciente2, Risco.LARANJA))
        self.assertEqual(self.fila.proximo().paciente.nome, "Ana")

    def test_fila_vazia(self):
        with self.assertRaises(FilaVaziaError):
            self.fila.proximo()

if __name__ == '__main__':
    unittest.main(verbosity=2)
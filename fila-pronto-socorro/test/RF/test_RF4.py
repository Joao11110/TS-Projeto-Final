import sys
sys.path.append("/home/joao/BTI/6º SEMESTRE/TS/fila-pronto-socorro/")

import unittest
from datetime import datetime
from main.error import ValidacaoError
from main.domain import Paciente, FilaAtendimento, Risco, Atendimento, FilaVaziaError, FichaAnalise

# --------------------------------------
# RF4: Chamar Próximo da Fila
# --------------------------------------

class TestRF4(unittest.TestCase):
    def test_chamar_proximo_fila_vazia(self):
        fila = FilaAtendimento()
        with self.assertRaises(FilaVaziaError):
            fila.proximo()

    def test_chamar_proximo_fila_nao_vazia(self):
        fila = FilaAtendimento()
        paciente = Paciente("Maria", "44444444444", "maria@exemplo.com", "04/04/2000")
        fila.inserir(Atendimento(paciente, Risco.VERDE))
        self.assertEqual(fila.proximo().paciente.nome, "Maria")

if __name__ == '__main__':
    unittest.main(verbosity=2)
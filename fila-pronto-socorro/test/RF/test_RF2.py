import sys
sys.path.append("/home/joao/BTI/6º SEMESTRE/TS/fila-pronto-socorro/")

import unittest
from datetime import datetime
from main.error import ValidacaoError
from main.domain import Paciente, FilaAtendimento, Risco, Atendimento, FilaVaziaError, FichaAnalise

# --------------------------------------
# RF2: Realizar Triagem
# --------------------------------------

class TestRF2(unittest.TestCase):
    def test_triagens_validas(self):
        casos = [
            (True, False, Risco.VERMELHO),
            (False, True, Risco.LARANJA),
        ]
        
        for risco_morte, gravidade_alta, risco_esperado in casos:
            with self.subTest(risco_morte=risco_morte, gravidade_alta=gravidade_alta):
                ficha = FichaAnalise(
                    risco_morte=risco_morte,
                    gravidade_alta=gravidade_alta,
                    gravidade_moderada=False,
                    gravidade_baixa=False
                )
                self.assertEqual(ficha.risco_morte, risco_esperado)

    def test_triagem_invalida(self):
        with self.assertRaises(ValidacaoError) as cm:
            FichaAnalise(
                risco_morte=False,
                gravidade_alta=True,
                gravidade_moderada=True,
                gravidade_baixa=False
            )
        self.assertIn("Combinação inválida", str(cm.exception))

if __name__ == '__main__':
    unittest.main(verbosity=2)